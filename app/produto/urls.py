from django.urls import path
from .views import CategoriaList, CategoriaMethodObject, ProdutoList, ProdutoMethodObject

urlpatterns = [
    path('categarias/',CategoriaList.as_view()),
    path('categoria/<int:id>',CategoriaMethodObject.as_view()),
    path('produtos/',ProdutoList.as_view()),
    path('produto/<int:id>',ProdutoMethodObject.as_view()),

]