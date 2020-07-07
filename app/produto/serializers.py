from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria

        #-- podemos usar os exemplos abaixo:
        #fields = ['campo1','campo2']
        #fields = '__all__'
        #exclude = ['campo1','campo2']
        #aqui vamos pegar

        #-- entao vamos selecionar todos os campos

        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'