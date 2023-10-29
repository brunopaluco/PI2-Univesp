# Generated by Django 4.2.6 on 2023-10-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_pedidos_anotacoes_alter_pedidos_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='anotacoes',
            field=models.CharField(blank=True, help_text='Insira as anotacoes da cotacao', null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='endereco',
            field=models.CharField(blank=True, help_text='Insira o endereco para despacho', null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='nome',
            field=models.CharField(help_text='Insira um nome valido: Nome e Sobrenomes', max_length=255, null=True),
        ),
    ]
