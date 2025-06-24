from rest_framework import serializers
from .models import Term

class TermSerializer(serializers.ModelSerializer):
    number = serializers.SerializerMethodField()

    class Meta:
        model = Term
        fields = [
            'id',
            'number',
            'english', 'russian', 'turkmen',
            'abbreviation', 'category',
            'description_en', 'description_ru', 'description_tm'
        ]

    def get_number(self, obj):
        return None

