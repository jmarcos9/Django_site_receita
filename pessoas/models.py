from django.db import models


class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
