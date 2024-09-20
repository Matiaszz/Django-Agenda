from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages, auth  # type: ignore
from django.contrib.auth.forms import AuthenticationForm


def register(req):

    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            messages.success(req, 'Usuário registrado')
            form.save()

            return redirect('contact:index')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(req, 'contact/register.html', context)


def login_view(req):
    form = AuthenticationForm(req)

    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(req, 'Logado com sucesso')
            print('User:', user)
            auth.login(req, user)
            return redirect('contact:index')
    context = {
        'form': form
    }
    return render(req, 'contact/login.html', context)


def logout_view(req):
    auth.logout(req)
    return redirect('contact:login')
