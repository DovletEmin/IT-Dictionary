from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Term
from .serializers import TermSerializer

class TermNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'english']

class TermsEnglishListView(generics.ListAPIView):
    queryset = Term.objects.all().order_by('english') 
    serializer_class = TermNameSerializer

class TermDetailView(generics.RetrieveAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer

class TermNameByLangSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class TermNameByLangView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "en")
        field_map = {"en": "english", "ru": "russian", "tm": "turkmen"}
        field = field_map.get(lang, "english")

        terms = Term.objects.all().order_by(field)
        result = [{"id": t.id, "name": getattr(t, field)} for t in terms]

        serializer = TermNameByLangSerializer(result, many=True)
        return Response(serializer.data)

class CategorySerializer(serializers.Serializer):
    category = serializers.CharField()

class CategoriesView(APIView):
    def get(self, request):
        categories = Term.objects.exclude(category="").order_by("category").values_list("category", flat=True).distinct()
        data = [{"category": c} for c in categories]
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)

class TermsCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()

class TermsCountView(APIView):
    def get(self, request):
        serializer = TermsCountSerializer({"count": Term.objects.count()})
        return Response(serializer.data)
