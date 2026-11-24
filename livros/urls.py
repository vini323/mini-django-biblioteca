"""
URLs DO APP. Este arquivo NÃO é criado pelo startapp: você cria na mão.
path(rota, view, name=apelido)
O 'name' permite usar {% url 'nome' %} nos templates.
"""
from django.urls import path
from . import views

app_name = "livros"   # namespace -> {% url 'livros:lista' %}

urlpatterns = [
    path("", views.lista_livros, name="lista"),
    path("livro/<int:pk>/", views.detalhe_livro, name="detalhe"),
    path("disponiveis/", views.disponiveis, name="disponiveis"),
    path("sobre/", views.sobre, name="sobre"),
]
