from django.urls import path
from .views import ClientList, ClientMethodObject, EnderecoList, EnderecoMethodObject

urlpatterns = [
    path('clientes/',ClientList.as_view()),
    path('cliente/<int:id>',ClientMethodObject.as_view()),
    path('enderecos/',EnderecoList.as_view()),
    path('endereco/<int:id>',EnderecoMethodObject.as_view()),

]