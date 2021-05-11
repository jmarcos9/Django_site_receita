from django.contrib import admin
from .models import Pessoa

class ExibirPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome_pessoa', 'email',)
    search_fields = ('nome_pessoa',)   
    list_display_links = ('id', 'nome_pessoa',)
    list_per_page = 2


admin.site.register(Pessoa, ExibirPessoa)