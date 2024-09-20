from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth  # type: ignore
from django.contrib.auth.forms import AuthenticationForm


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Usuário registrado')
            form.save()

            return redirect('contact:index')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'contact/register.html', context)


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    context = {
        'form': form
    }
    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            context
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    if not form.is_valid():

        return render(
            request,
            'contact/register.html',
            context
        )
    form.save()
    return redirect('contact:user_update')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Logado com sucesso')
            auth.login(request, user)
            return redirect('contact:index')
    context = {
        'form': form,
    }
    return render(request, 'contact/login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
