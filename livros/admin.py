"""
ADMIN = registra os models para aparecerem no painel /admin.
(Passo 10 do quadro: "add admin")
Sem registrar aqui, o model existe no banco mas NÃO aparece no painel.
"""
from django.contrib import admin
from .models import Categoria, Livro, Leitor, Emprestimo

# Forma simples:
admin.site.register(Categoria)


# Forma personalizada (com decorator):
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "categoria", "disponivel")  # colunas da lista
    list_filter = ("disponivel", "categoria")                             # filtros laterais
    search_fields = ("titulo", "autor")                                   # caixa de busca


@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone")
    search_fields = ("nome", "email")


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("livro", "leitor", "data_emprestimo", "data_devolucao")
    list_filter = ("data_emprestimo",)
