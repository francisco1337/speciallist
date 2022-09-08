from distutils.command import upload
from email.policy import default
from enum import unique
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

class Country(models.Model):
    
    country = models.CharField("Pais", max_length=100, null=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Paises"

    def __str__(self):
        return self.country

class State(models.Model):
    
    country = models.ForeignKey(Country, verbose_name="Pais", on_delete=models.CASCADE, null=True ) 
    state = models.CharField("Estado", max_length=100, null=True, blank=False)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __str__(self):
        return self.country.country+"-"+self.state

class Town(models.Model):
    
    country = models.ForeignKey(Country, verbose_name="Pais", on_delete=models.CASCADE, null=True)
    state = models.ForeignKey(State, verbose_name="Estado", on_delete=models.CASCADE, null=True)
    town = models.CharField("Ciudad", max_length=100, null=True, blank=False)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.country.country+"-"+self.state.state+"-"+self.town

class Rol(models.Model):

    name = models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField("Descripcion", max_length=400)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def get_short_name(self):
        return self.name

    def get_full_name(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    
    image = models.ImageField(upload_to ='uploads/image/users/', blank=True, null=True)
    names = models.CharField("Nombres", max_length=200)
    lastnames = models.CharField("Apellidos", max_length=200)
    gender = models.CharField("Sexo",max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    email = models.EmailField("Correo",unique=True, max_length=150)
    curp = models.CharField("CURP", max_length=200, blank=True, null=True) 
    rfc = models.CharField("RFc", max_length=70, blank=True, null=True) 
    estadoCivil = models.CharField("Estado Civil", max_length=70, blank=True, null=True) 
    estado = models.CharField("Estado", max_length=70, blank=True, null=True)  
    municipio = models.CharField("Municipio", max_length=70, blank=True, null=True)  
    colonia = models.CharField("Colonia", max_length=70, blank=True, null=True)  
    calle = models.CharField("Calle", max_length=70, blank=True, null=True)  
    numero = models.CharField("Numero", max_length=70, blank=True, null=True)  
    # img = models.CharField("Imagen", max_length=150, null=True)  
    rol = models.ForeignKey(Rol, verbose_name="Rol", on_delete=models.CASCADE, blank=True, null=True)
    google = models.BooleanField("Google", default=False)  
    facebook = models.BooleanField("Facebook", default=False)  
    codregistro = models.CharField("Codigo de Verificación",max_length=6, blank=True, null=True)
    #
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['names','lastnames',]

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def get_short_name(self):
        return self.names
    
    def get_full_name(self):
        return self.names + ' ' + self.lastnames



