# Generated by Django 3.2.2 on 2021-05-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webreceitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='data_receita',
            new_name='data_receitas',
        ),
    ]