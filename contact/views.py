from django.shortcuts import render
# Create your views here.


def index(req):

    #                  pagina do html
    return render(req, 'contact/index.html', )
