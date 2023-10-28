# Generated by Django 4.2.6 on 2023-10-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidos',
            options={'ordering': ['nome', 'criacao'], 'verbose_name': 'Pedidos recebidos'},
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='arquivo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='email',
            field=models.EmailField(help_text='Insira um e-mail valido: usuario@dominio', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='mensagem',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='nome',
            field=models.CharField(help_text='Insira um nome valido: Nome e Sobrenomes', max_length=255),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]