# Generated by Django 2.1 on 2018-09-08 01:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('melhoridade', '0003_banco_orgao_prazo_produto_promotora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True)),
                ('valor', models.FloatField()),
                ('detalhes', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melhoridade.Funcionario')),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melhoridade.Banco')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melhoridade.Cliente')),
                ('parcelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melhoridade.Prazo')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melhoridade.Produto')),
                ('promotora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='melhoridade.Promotora')),
            ],
        ),
    ]
