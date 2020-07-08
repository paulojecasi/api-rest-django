from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer

class ClientList(APIView):

   def get(self,request):
       cliente = Cliente.objects.all()
       serializer = ClienteSerializer(cliente, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = ClienteSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientMethodObject(APIView):

    def get_object(self, id):
        try:
            return Cliente.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        cliente = self.get_object(id)
        serializer = ClienteSerializer(cliente, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        cliente=self.get_object(id)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class EnderecoList(APIView):

   def get(self,request):
       endereco = Endereco.objects.all()
       serializer = EnderecoSerializer(endereco, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = EnderecoSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)


class EnderecoMethodObject(APIView):

    def get_object(self, id):
        try:
            return Endereco.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        endereco = self.get_object(id)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        endereco = self.get_object(id)
        serializer = EnderecoSerializer(endereco, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        endereco=self.get_object(id)
        endereco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







