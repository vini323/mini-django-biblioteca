"""
URLs DO PROJETO (principal).
Ele não define as páginas do app diretamente: usa include() para
"delegar" para o urls.py de cada app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),     # painel administrativo
    path("", include("livros.urls")),    # tudo o resto vai pro app livros
]
