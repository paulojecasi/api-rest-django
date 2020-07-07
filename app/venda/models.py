from django.db import models

# Create your models here.

class Venda(models.Model):
    tipo_CHOIDES = (
        (1, 'Atacado'),
        (2, 'Varejo')
    )

    funcionario = models.ForeignKey('funcionario.Funcionario',
                                  related_name='venda_funcionario',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  verbose_name='Categoria')
    cliente = models.ForeignKey('cliente.Cliente',
                                    related_name='venda_cliente',
                                    on_delete=models.CASCADE,
                                    null=True,
                                    verbose_name='Categoria')

    criado_em = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Vendas'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return '{}'.format(self.funcionario)


class VendasProd(models.Model):
    sexo_CHOIDES = (
        (1, 'MASCULINO'),
        (2, 'FEMININO')
    )


    venda= models.ForeignKey(Venda, related_name='vendasprod_venda',
                                    on_delete=models.CASCADE,
                                    null=True,
                                    verbose_name='Venda')
    produto = models.ForeignKey('produto.Produto',
                                related_name='vendasprod_produto',
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='Produto')

    quantidade = models.PositiveIntegerField(null=False, default=1)


    class META:
        verbose_name = 'Produto da Venda'
        verbose_name_plural = 'Produtos da Venda'

    def __str__(self):
        return {}.format(self.venda)



