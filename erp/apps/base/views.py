from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Usuario

from utilities import tools

# Create your views here.

def home(request):
    return HttpResponse('''<h1>Hola </h1> </br> 
                        <button> <a href="accounts/login"> Ir a login </a> </button>''')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def settings(request):
    usuario = Usuario.get_usuario(request)
    return render(request, 'settings.html', context= {'usuario':usuario})


def update_personal_info(request):
    if request.FILES:
        print(request.FILES)
        usuario = Usuario.get_usuario(request)
        usuario.profile_image = request.FILES['profile_image']
        usuario.save()
    usuario = Usuario.filter_usuario(request)
    data = tools.remove_csrftoken(request.POST)
    usuario.update(**data)
    messages.success(request, "Tu información profesional fue actualizada correctamente.")
    return redirect('settings') 
