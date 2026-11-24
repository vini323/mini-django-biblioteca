"""
SETTINGS = configurações do projeto inteiro.
Os pontos que mais caem em prova estão marcados com  # <<<
"""
from pathlib import Path

# Pasta raiz do projeto (onde está o manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta usada em criptografia/sessões. Nunca publicar a de produção.
SECRET_KEY = "django-insecure-troque-esta-chave-em-producao"

# DEBUG=True mostra erros detalhados. Em produção deve ser False.  # <<<
DEBUG = True

# Domínios que podem servir o site (obrigatório quando DEBUG=False)
ALLOWED_HOSTS = []

# Apps ativos no projeto. Todo app criado com startapp PRECISA entrar aqui.  # <<<
INSTALLED_APPS = [
    "django.contrib.admin",         # painel /admin
    "django.contrib.auth",          # usuários e permissões
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "livros",                        # <<< nosso app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Arquivo de URLs principal do projeto  # <<<
ROOT_URLCONF = "biblioteca.urls"

# Onde o Django procura os templates (HTML)  # <<<
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # pasta global de templates
        "APP_DIRS": True,                  # também procura em <app>/templates/
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "biblioteca.wsgi.application"

# Banco de dados. Padrão: SQLite (arquivo db.sqlite3)  # <<<
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Idioma e fuso horário  # <<<
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Arquivos estáticos (CSS, JS, imagens)
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
