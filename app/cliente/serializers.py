from rest_framework import serializers
from .models import Endereco, Cliente

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco

        #-- podemos usar os exemplos abaixo:
        #fields = ['campo1','campo2']
        #fields = '__all__'
        #exclude = ['campo1','campo2']
        #aqui vamos pegar

        #-- entao vamos selecionar todos os campos

        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'