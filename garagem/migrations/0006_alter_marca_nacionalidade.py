# Generated by Django 4.1.7 on 2023-03-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_acessorio_cor_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]