# Generated by Django 3.2.2 on 2021-05-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webreceitas', '0009_receita_foto_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
