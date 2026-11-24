"""
ADMIN = registra os models para aparecerem no painel /admin.
(Passo 10 do quadro: "add admin")
Sem registrar aqui, o model existe no banco mas NÃO aparece no painel.
"""
from django.contrib import admin
from .models import Categoria, Livro

# Forma simples:
admin.site.register(Categoria)


# Forma personalizada (com decorator):
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "categoria", "disponivel")  # colunas da lista
    list_filter = ("disponivel", "categoria")                             # filtros laterais
    search_fields = ("titulo", "autor")                                   # caixa de busca
