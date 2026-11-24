# Mini projeto Django: Biblioteca

## Rodar (Windows)
```
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Acesse http://127.0.0.1:8000/ e http://127.0.0.1:8000/admin/

## Onde está cada tema
- settings: biblioteca/settings.py (INSTALLED_APPS, TEMPLATES, DATABASES, LANGUAGE_CODE)
- URLs: biblioteca/urls.py (include) e livros/urls.py (path)
- views: livros/views.py
- templates: templates/base.html e livros/templates/livros/
- models: livros/models.py
- admin: livros/admin.py
