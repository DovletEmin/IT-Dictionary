from rest_framework import serializers

from .models import Term


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = "__all__"



class TermNameSerializer(serializers.ModelSerializer):
    model = Term
    fields = ("id", "english")