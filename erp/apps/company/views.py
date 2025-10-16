from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import transaction

from apps.company.models import Company, Collaborator

from utilities import tools
# Create your views here.


def add_company(request):
    if request.method == 'GET':
        return render(request, 'company/add_company.html')
    else:
        data = tools.remove_csrftoken(request.POST)
        with transaction.atomic():
            company = Company.objects.create(**data)
            Collaborator.objects.create(
                role='owner',
                usuario=request.user.usuario,
                company=company,
                can_edit=True,
                can_delete=True
            )
        messages.success(request, f'Empresa "{company.name}" creada con éxito.')
        return redirect('add_company')
    

def view_company(request):
    companies = request.user.usuario.collaborator_set.all()
    "implementar vien esto"
    return render(request,'company/view_company.html', {'companies',companies})