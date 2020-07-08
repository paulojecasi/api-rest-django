from django.db import models

# Create your models here.

class Venda(models.Model):
    funcionario = models.ForeignKey('funcionario.Funcionario',
                                  related_name='venda_funcionario',
                                  on_delete=models.CASCADE,
                                  null=True)
    cliente = models.ForeignKey('cliente.Cliente',
                                    related_name='venda_cliente',
                                    on_delete=models.CASCADE,
                                    null=True)

    criado_em = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Vendas'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return '{}'.format(self.funcionario)


class VendasProd(models.Model):

    venda= models.ForeignKey(Venda, related_name='vendasprod_venda',
                                    on_delete=models.CASCADE,
                                    null=True)
    produto = models.ForeignKey('produto.Produto',
                                related_name='vendasprod_produto',
                                on_delete=models.CASCADE,
                                null=True)

    quantidade = models.PositiveIntegerField(null=False, default=1)


    class META:
        verbose_name = 'Produto da Venda'
        verbose_name_plural = 'Produtos da Venda'

    def __str__(self):
        return {}.format(self.venda)



