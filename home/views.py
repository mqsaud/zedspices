from django.shortcuts import render
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ View to return about page"""
    return render(request, 'home/about.html')


def contact(request):
    """ View to return contact page"""
    return render(request, 'home/contact.html')
