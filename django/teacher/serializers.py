from argparse import ArgumentDefaultsHelpFormatter
from dataclasses import fields
from rest_framework import serializers
from teacher.models import Aula, Professor
from django.forms import ValidationError

class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class CadastrarAulaSerializers(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    nome = serializers.CharField(max_length=100)

    def validate_nome(self, value):
        if len(value) < 3:
           raise ValidationError('deve ter pelo menos três caracteres')
        return value 
              

class AulaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'     