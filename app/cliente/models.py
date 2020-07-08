from django.db import models

# Create your models here.

class Endereco(models.Model):
    endereco =models.CharField(max_length=100)
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=80)
    uf = models.CharField(max_length=40)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.endereco


class Cliente(models.Model):

    sexo_CHOIDES = (
        (1, 'MASCULINO'),
        (2, 'FEMININO'),
    )

    tipo_cliente_CHOICES = (
        (1, 'PESSOA FISICA'),
        (2, 'PESSOA JURIDICA'),
    )
    endereco = models.ForeignKey(Endereco, related_name='endereco_cliente',
                                on_delete=models.CASCADE,
                                null=True)
    nome = models.CharField(max_length=100)
    sexo = models.IntegerField(choices=sexo_CHOIDES)
    data_nasc = models.DateField(auto_now=False)
    telefone = models.CharField(max_length=30)
    tipo = models.IntegerField(choices= tipo_cliente_CHOICES)

    class META:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

