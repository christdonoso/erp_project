from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('''<h1>Hola </h1> </br> 
                        <button> <a href="accounts/login"> Ir a login </a> </button>''')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def settings(request):
    return render(request, 'settings.html')