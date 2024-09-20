from django.shortcuts import render
from contact.models import Contact


def contact(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:30]
    context = {
        'contacts': contacts
    }
    return render(request, 'contact/contact.html', context)
