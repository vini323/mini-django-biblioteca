@echo off
cd /d "%~dp0"
echo Criando migracoes das tabelas novas...
venv\Scripts\python.exe manage.py makemigrations
echo.
echo Aplicando no banco...
venv\Scripts\python.exe manage.py migrate
echo.
echo Pronto! Pode fechar esta janela.
pause
