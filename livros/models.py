"""
MODELS = classes Python que viram TABELAS no banco.
Cada atributo = uma coluna.
Depois de criar/alterar um model:
    python manage.py makemigrations   (gera o arquivo de migração)
    python manage.py migrate          (aplica no banco)
"""
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):          # como o objeto aparece no admin
        return self.nome


class Livro(models.Model):
    titulo = models.CharField("Título", max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    # Relacionamento: vários livros -> uma categoria
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="livros"
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} ({self.ano})"


class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)  # blank=True -> opcional

    class Meta:
        verbose_name_plural = "Leitores"

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    # Tabela que liga Livro e Leitor (duas ForeignKeys)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE, related_name="emprestimos")
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)  # vazio = ainda não devolvido

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return f"{self.livro.titulo} -> {self.leitor.nome}"
