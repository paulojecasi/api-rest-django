from django.db import models

# Create your models here.

class Endereco(models.Model):
    endereco =models.CharField(max_length=100, verbose_name= "Endereco")
    bairro = models.CharField(max_length=80, verbose_name= "Bairro")
    cidade = models.CharField(max_length=80, verbose_name= "Cidade")
    uf = models.CharField(max_length=40, verbose_name="Uf")
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return '{}'.format(self.endereco)


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
                                null=True,
                                verbose_name='Usuario')
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sexo = models.IntegerField(max_length=1, choices=sexo_CHOIDES, verbose_name="Sexo")
    data_nasc = models.DateField(auto_now=False)
    telefone = models.CharField(max_length=30, verbose_name=" Telefone")
    tipo = models.IntegerField(max_length=1, choices= tipo_cliente_CHOICES)

    class META:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return {}.format(self.nome)

