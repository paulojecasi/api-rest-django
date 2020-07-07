from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Setor, Funcionario
from .serializers import SetorSerializer, FuncionarioSerializer

class SetorList(APIView):

   def get(self,request):
       setor = Setor.objects.all()
       serializer = SetorSerializer(Setor, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = SetorSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)

class SetorMethodObject(APIView):

    def get_object(self, id):
        try:
            return Setor.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        setor = self.get_object(id)
        serializer = SetorSerializer(setor)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        setor = self.get_object(id)
        serializer = SetorSerializer(setor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        setor=self.get_object(id)
        setor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class FuncionarioList(APIView):

   def get(self,request):
       funcionario = Funcionario.objects.all()
       serializer = FuncionarioSerializer(funcionario, many=True)
       print(serializer)
       return Response(serializer.data)

   def post(self, request):
       serializer = FuncionarioSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_CREATED)


class FuncionarioMethodObject(APIView):

    def get_object(self, id):
        try:
            return Funcionario.objects.get(id=id)
        except:
            raise Http404

    #consultar
    def get(self,request, id):
        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    #edição
    def put(self, request, id):
        funcionario = self.get_object(id)
        serializer = FuncionarioSerializer(funcionario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #deletar
    def delete(self, request, id):
        funcionario=self.get_object(id)
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


