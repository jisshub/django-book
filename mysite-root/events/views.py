from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h1>My Club Event Calender</h1>')

# path(route, view)
