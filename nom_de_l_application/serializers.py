from rest_framework import serializers
from .models import MonFormulaire

class MonFormulaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonFormulaire
        fields = '__all__'