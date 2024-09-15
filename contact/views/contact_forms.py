from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


def create(req):
    post = req.POST
    return render(req, 'contact/create.html')
