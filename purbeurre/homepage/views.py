from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')


def mentions(request):
    return render(request, 'homepage/mentions-legales.html')
