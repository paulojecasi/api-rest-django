from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Venda, VendasProd
from .serializers import VendaSerializer, VendasProdSerializer

class VendaList(APIView):

   def get(self,request):
       venda = Venda.objects.all()
       serializer = VendaSerializer(venda, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = VendaSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)

class VendaMethodObject(APIView):

    def get_object(self, id):
        try:
            return Venda.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        venda = self.get_object(id)
        serializer = VendaSerializer(venda)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        venda = self.get_object(id)
        serializer = VendaSerializer(venda, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        venda=self.get_object(id)
        venda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class VendasProdList(APIView):

   def get(self,request):
       vendasprod = VendasProd.objects.all()
       serializer = VendasProdSerializer(vendasprod, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = VendasProdSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendasProdMethodObject(APIView):

    def get_object(self, id):
        try:
            return VendasProd.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        vendasprod = self.get_object(id)
        serializer = VendasProdSerializer(vendasprod)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        vendasprod = self.get_object(id)
        serializer = VendasProdSerializer(vendasprod, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        vendasprod=self.get_object(id)
        vendasprod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



