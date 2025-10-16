from django.db import models
from apps.base.models import Usuario

# Create your models here.

class Company(models.Model):
    '''
    Representa una empresa dentro del ERP.
    Es el núcleo sobre el cual se gestionan colaboradores, proyectos, etc.
    '''

    name = models.CharField(max_length=255, )
    rut = models.CharField(max_length=20, unique=True, )
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, )
    website = models.URLField(blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Collaborator(models.Model):
    '''
    Relación entre un usuario (perfil) y una empresa.
    Define su rol, permisos y estado dentro de esa empresa.
    '''
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    ROLE_CHOICES = [
        ('owner', 'Dueño'),
        ('admin', 'Administrador'),
        ('manager', 'Encargado'),
        ('employee', 'Colaborador'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    can_view = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.user.get_full_name() or self.usuario.user.username} - {self.company.name} ({self.get_role_display()})'