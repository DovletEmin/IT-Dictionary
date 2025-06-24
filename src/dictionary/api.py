from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q
from .serializers import TermSerializer
from .models import Term



LANG_MAP = {
    'en': ('english', 'description_en'),
    'ru': ('russian', 'description_ru'),
    'tm': ('turkmen', 'description_tm'),
}

@api_view(['GET'])
def get_terms(request, lang='en'):
    term_field, desc_field = LANG_MAP.get(lang, LANG_MAP['en'])

    queryset = Term.objects.all().order_by('id')

    # Фильтрация
    search = request.GET.get('search')
    if search:
        queryset = queryset.filter(**{f"{term_field}__icontains": search})

    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(category__iexact=category)

    # Пагинация
    page = int(request.GET.get('page', 1))
    page_size = 30
    start = (page - 1) * page_size
    end = start + page_size
    paginated_queryset = queryset[start:end]

    # Формируем результат с номерами
    data = [
        {
            'id': term.id,
            'number': start + i + 1,
            'term': getattr(term, term_field),
            'abbreviation': term.abbreviation,
            'category': term.category,
            'description': getattr(term, desc_field),
        }
        for i, term in enumerate(paginated_queryset)
    ]

    return Response({
        'count': queryset.count(),
        'page': page,
        'page_size': page_size,
        'results': data
    })



class TermPagination(PageNumberPagination):
    page_size = 30

@api_view(['GET'])
def all_terms_view(request):
    paginator = TermPagination()
    queryset = Term.objects.all().order_by('id')

    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(category__iexact=category)

    search = request.GET.get('search')
    if search:
        queryset = queryset.filter(
            Q(english__icontains=search) |
            Q(russian__icontains=search) |
            Q(turkmen__icontains=search)
        )

    page = paginator.paginate_queryset(queryset, request)
    start_index = (paginator.page.number - 1) * paginator.page_size

    data = [
        {
            'id': term.id,
            'number': start_index + idx + 1,
            'english': term.english,
            'russian': term.russian,
            'turkmen': term.turkmen,
            'abbreviation': term.abbreviation,
            'category': term.category,
            'description_en': term.description_en,
            'description_ru': term.description_ru,
            'description_tm': term.description_tm,
        }
        for idx, term in enumerate(page)
    ]
    return paginator.get_paginated_response(data)


class AllTermsView(ListAPIView):
    serializer_class = TermSerializer
    pagination_class = TermPagination

    def get_queryset(self):
        queryset = Term.objects.all().order_by('english')

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(english__icontains=search) |
                Q(russian__icontains=search) |
                Q(turkmen__icontains=search)
            )
        return queryset
    
class TermDetailView(RetrieveAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    lookup_field = 'id'
    
