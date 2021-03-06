# Generated by Django 3.0.8 on 2020-07-06 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('bairro', models.CharField(max_length=80, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=80, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=40, verbose_name='Uf')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sexo', models.IntegerField(choices=[(1, 'MASCULINO'), (2, 'FEMININO')], max_length=1, verbose_name='Sexo')),
                ('data_nasc', models.DateField()),
                ('telefone', models.CharField(max_length=30, verbose_name=' Telefone')),
                ('tipo', models.IntegerField(choices=[(1, 'PESSOA FISICA'), (2, 'PESSOA JURIDICA')], max_length=1)),
                ('endereco', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_cliente', to='cliente.Endereco', verbose_name='Usuario')),
            ],
        ),
    ]
