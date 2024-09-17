from django.shortcuts import render, redirect
from contact.forms import ContactForm


def create(req):
    if req.method == 'POST':
        form = ContactForm(req.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()

            # ----------
            # before saving, do something; afterward, save
            # contact = form.save(commit=False)
            # contact.show = True
            # contact.save()
            return redirect('contact:create')

        return render(req, 'contact/create.html', context)

    context = {
        'form': ContactForm()
    }
    return render(req, 'contact/create.html', context)
