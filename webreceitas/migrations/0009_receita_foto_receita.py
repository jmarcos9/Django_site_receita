# Generated by Django 3.2.2 on 2021-05-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webreceitas', '0008_receita_publicar'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]
