from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages  # type: ignore


def register(req):

    # messages.warning(req, 'aviso')
    # messages.info(req, 'informacao')
    # messages.error(req, 'erro')
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
