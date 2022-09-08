from datetime import timedelta, datetime 

from django.db import models

from applications.users.models import  User, Country, State, Town
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify

# Create your models here.

class Title(TimeStampedModel):

    title = models.CharField("Titulo", max_length=150)

    class Meta:
        verbose_name = "Titulo"
        verbose_name_plural = "Titulos"

    def __str__(self):
        return self.title


class Specialism(TimeStampedModel):

    specialism = models.CharField("Especialidad", max_length=150)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.specialism

class Specialist(TimeStampedModel):
 
    image = models.ImageField(upload_to ='uploads/image/specialist/', blank=True, null=True)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    specialism = models.ForeignKey(Specialism, blank=True, null=True, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, blank=True, null=True, on_delete=models.CASCADE)
    professional_license = models.CharField("Licencia", blank=True, null=True, max_length=40)
    description_content = RichTextField(verbose_name="Descripción", blank=True, null=True, config_name='portal_config')
    phrase = models.CharField(verbose_name="Frase", max_length=200,  default="", blank=True, null=True)
    slug = models.SlugField(editable=True, max_length=300,blank=True, null=True)

    class Meta:
        verbose_name = "Especialista"
        verbose_name_plural = "Especialistas"


    def __str__(self):
        return str(self.id)+"-"+self.user.names

    def save(self, *args, **kwargs):
        slug_unique = '%s  %s' % (self.user.names, self.user.lastnames) 
        self.slug = slugify(slug_unique)

        super(Specialist, self).save(*args, **kwargs)


class Clinic(TimeStampedModel):

    principal_image = models.ImageField(upload_to ='uploads/image/clinic/', blank=True, null=False)
    second_image = models.ImageField(upload_to ='uploads/image/clinic/', blank=True, null=False)
    third_image = models.ImageField(upload_to ='uploads/image/clinic/', blank=True, null=False)
    fourth_image = models.ImageField(upload_to ='uploads/image/clinic/', blank=True, null=False)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE )
    clinic = models.CharField("NombreClinica", max_length=200, blank=True, null=False)
    country = models.ForeignKey(Country, verbose_name="Pais", on_delete=models.CASCADE, null=True, blank=False)
    state = models.ForeignKey(State,  verbose_name="Estado", on_delete=models.CASCADE, null=True, blank=False)
    town = models.ForeignKey(Town,  verbose_name="Ciudad/Municipio", on_delete=models.CASCADE, null=True, blank=False)
    postal_code = models.IntegerField("Codigo postal", null=True, blank=False, default=None)
    suburb = models.CharField("Colonia", max_length=1000, null=True, blank=False, default=None)
    Street = models.CharField("Calle", max_length=1000, null=True, blank=False, default=None)
    number = models.IntegerField("Numero", null=True, default=True, blank=False)
    map_iframe = models.CharField("Google map", max_length=1000, null=True, blank=False, default=None)
    description = RichTextField(verbose_name="Descripción", blank=True, null=False, config_name='portal_config')
    other_Data = RichTextField(verbose_name="Otros datos", blank=True, null=False, config_name='portal_config')

    class Meta:
        verbose_name = "Clinica"
        verbose_name_plural = "Clinicas"

    def __str__(self):
        return str(self.id)+" "+self.clinic



    

class Schedule(TimeStampedModel):

    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)
    lunes = models.JSONField("Lunes", blank=True, null=True)
    martes = models.JSONField("Martes", blank=True, null=True)
    miercoles = models.JSONField("Miercoles", blank=True, null=True)
    jueves = models.JSONField("Jueves", blank=True, null=True)
    viernes = models.JSONField("Viernes", blank=True, null=True)
    sabado = models.JSONField("Sabado", blank=True, null=True)
    domingo = models.JSONField("Domingo", blank=True, null=True)

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return str(self.specialist.user)+"-"+self.clinic.clinic

class Availability(TimeStampedModel):

    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)
    date = models.DateField('Fecha', default=None)
    availability = models.JSONField("Availability", null=True)

    class Meta:
        verbose_name = "Disponibilidad"
        verbose_name_plural = "Disponibilidades"

    def __str__(self):
        return self.specialist+"-"+self.clinic+"-"+"Disponibilidad"

class Meeting_topic(TimeStampedModel):

    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)
    topic = models.CharField("Asuntos/Temas", max_length=150, null=True)

    class Meta:
        verbose_name = "Asunto de cita"
        verbose_name_plural = "Asuntos de citas"

    def __str__(self):
        return self.topic


class Meeting(TimeStampedModel):

    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Meeting_topic, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField("Fecha", null=True)
    time = models.TimeField("Hora",  null=True)
    comments = models.TextField("Comentario", max_length=400, null=True)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

    def __str__(self):
        return str(self.id)