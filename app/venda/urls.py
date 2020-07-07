from django.urls import path
from .views import VendaList, VendaMethodObject, VendasProdList, VendasProdMethodObject

urlpatterns = [
    path('vendas/',VendaList.as_view()),
    path('venda/<int:id>',VendaMethodObject.as_view()),
    path('vendasprod/',VendasProdList.as_view()),
    path('vendaprod/<int:id>',VendasProdMethodObject.as_view()),

]