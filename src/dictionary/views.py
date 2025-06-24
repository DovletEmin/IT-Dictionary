from django.http import JsonResponse
from .models import Term

LANG_MAP = {
    'en': ('english', 'description_en'),
    'ru': ('russian', 'description_ru'),
    'tm': ('turkmen', 'description_tm'),
}

def get_terms(request, lang='en'):
    term_field, desc_field = LANG_MAP.get(lang, LANG_MAP['en'])

    queryset = Term.objects.all()

    # Поиск по ключевому слову
    search = request.GET.get('search')
    if search:
        queryset = queryset.filter(
            **{f"{term_field}__icontains": search}
        )

    # Фильтрация по категории
    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(category__iexact=category)

    data = [
        {
            'term': getattr(term, term_field),
            'abbreviation': term.abbreviation,
            'category': term.category,
            'description': getattr(term, desc_field),
        }
        for term in queryset
    ]
    return JsonResponse(data, safe=False)

