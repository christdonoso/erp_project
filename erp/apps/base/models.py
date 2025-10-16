from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Usuario(models.Model):

    USER_TYPE = [
        ('COLAB','Colaborador'),
        ('ADMIN', 'Administrador'),
        ('OWNER','Dueño')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')
    personal_info = models.TextField()
    email = models.EmailField(max_length=50)
    sex = models.EmailField(max_length=50,null=True, blank=True)
    birth_date = models.DateField()
    address = models.CharField(max_length=150)
    region = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    user_type = models.CharField(max_length=15,choices = USER_TYPE)
    degree = models.CharField(max_length=150,null=True, blank=True)
    institution = models.CharField(max_length=150,null=True, blank=True)
    graduation_year = models.CharField(max_length=50,null=True, blank=True)
    years_experience = models.CharField(max_length=50,null=True, blank=True)
    specialization = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    courses = models.TextField(blank=True)
 
    def __str__(self):
        return self.names + ' ' + self.last_names
    
    @staticmethod
    def get_usuario(request):
        user = request.user
        usuario = Usuario.objects.get(user = user)
        return usuario

    @staticmethod
    def filter_usuario(request):
        user = request.user
        usuario = Usuario.objects.filter(user = user)
        return usuario
    