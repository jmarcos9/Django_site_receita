from django.contrib import admin
from .models import Receita

class ExibirReceita(admin.ModelAdmin):
    list_display= ('id', 'nome_receita', 'categoria',  'tempo_preparo', 'pessoa', 'publicar')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 10
    list_editable = ('publicar',)

admin.site.register(Receita, ExibirReceita)
