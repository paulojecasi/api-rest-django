from rest_framework import serializers
from .models import Setor, Funcionario

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor

        #-- podemos usar os exemplos abaixo:
        #fields = ['campo1','campo2']
        #fields = '__all__'
        #exclude = ['campo1','campo2']
        #aqui vamos pegar

        #-- entao vamos selecionar todos os campos

        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'