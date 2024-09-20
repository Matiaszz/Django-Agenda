from django.shortcuts import render
from contact.models import Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def history(request):
    contacts = Contact.objects.filter(
        show=True, owner=request.user).order_by('-id')
    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'History - ',
    }

    return render(request, 'contact/history.html', context)
