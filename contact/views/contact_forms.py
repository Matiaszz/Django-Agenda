from django.shortcuts import render
from contact.forms import ContactForm


def create(req):
    if req.method == 'POST':

        context = {
            'form': ContactForm(req.POST)
        }

        return render(req, 'contact/create.html', context)

    context = {
        'form': ContactForm()
    }
    return render(req, 'contact/create.html', context)
