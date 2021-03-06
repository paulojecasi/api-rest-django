# Generated by Django 3.0.8 on 2020-07-08 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20200708_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_cliente', to='cliente.Endereco'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'MASCULINO'), (2, 'FEMININO')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'PESSOA FISICA'), (2, 'PESSOA JURIDICA')]),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='endereco',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(max_length=40),
        ),
    ]
