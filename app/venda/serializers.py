from rest_framework import serializers
from .models import Venda, VendasProd

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda

        #-- podemos usar os exemplos abaixo:
        #fields = ['campo1','campo2']
        #fields = '__all__'
        #exclude = ['campo1','campo2']
        #aqui vamos pegar

        #-- entao vamos selecionar todos os campos

        fields = '__all__'


class VendasProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendasProd
        fields = '__all__'