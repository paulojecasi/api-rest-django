from django.db import models

# Create your models here.

class Setor(models.Model):
    tipo_CHOIDES = (
        (1, 'Vendas Externas'),
        (2, 'Vendas Internas')
    )
    nome = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=tipo_CHOIDES)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'

    def __str__(self):
        return '{}'.format(self.nome)


class Funcionario(models.Model):
    sexo_CHOIDES = (
        (1, 'MASCULINO'),
        (2, 'FEMININO')
    )


    setor = models.ForeignKey(Setor, related_name='funcionario_setor',
                                    on_delete=models.CASCADE,
                                    null=True)
    nome = models.CharField(max_length=100)
    sexo = models.IntegerField(choices=sexo_CHOIDES)
    data_nasc = models.DateField(auto_now=False)
    cpf = models.PositiveIntegerField()

    class META:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return {}.format(self.nome)


from django.db import models

# Create your models here.
