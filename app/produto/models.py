from django.db import models

# Create your models here.

class Categoria(models.Model):
    tipo_CHOIDES = (
        (1, 'Atacado'),
        (2, 'Varejo')
    )
    nome = models.CharField(max_length=100)
    tipo_venda = models.IntegerField(choices=tipo_CHOIDES)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{}'.format(self.nome)


class Produto(models.Model):
    categoria= models.ForeignKey(Categoria, related_name='produto_categoria',
                                    on_delete=models.CASCADE,
                                    null=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField()

    class META:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return {}.format(self.nome)



