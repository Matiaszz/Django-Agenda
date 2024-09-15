from django.shortcuts import render
from contact.models import Contact


def contact(req):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:30]
    context = {
        'contacts': contacts
    }
    return render(req, 'contact/contact.html', context)
