"""
VIEWS = funções (ou classes) que recebem uma requisição (request)
e devolvem uma resposta (HttpResponse ou render de template).
Fluxo: URL -> VIEW -> (MODEL) -> TEMPLATE -> resposta
"""
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Livro


# 1) View mais simples possível: devolve texto puro
def sobre(request):
    return HttpResponse("Mini projeto Django - Biblioteca")


# 2) View que busca no banco e renderiza um template
def lista_livros(request):
    livros = Livro.objects.all()                      # SELECT * FROM livro
    contexto = {"livros": livros, "total": livros.count()}
    return render(request, "livros/lista.html", contexto)


# 3) View que recebe parâmetro pela URL (<int:pk>)
def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)           # 404 se não existir
    return render(request, "livros/detalhe.html", {"livro": livro})


# 4) View com filtro
def disponiveis(request):
    livros = Livro.objects.filter(disponivel=True)
    return render(request, "livros/lista.html", {"livros": livros, "total": livros.count()})
