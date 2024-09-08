Iniciar o projeto Django

```
python -m venv .venv
. venv/bin/activate or . venv\scripts\activate
pip install django
django-admin startproject project .
```

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```
Depois de dar o primeiro push...

```
.\.venv\scripts\activate
python manage.pt startapp contact
```
ir até .\contact\apps.py
verificar o "name"

ir até .\project\settings.py em INSTALLED_APPS e adicionar o "name" que foi verificado