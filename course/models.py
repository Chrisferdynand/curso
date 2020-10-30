from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator
# Create your models here.
class Programa(models.Model):
        id = models.AutoField(primary_key = True)
        nombre = models.CharField('Nombre del expositor', max_length = 150)
        tema = models.TextField('Título del tema', validators = [MaxLengthValidator(1000)])
        FechaHora = models.DateTimeField(null = True, unique=True, help_text='Fecha y hora de la charla')
        enlaceMeet = models.URLField(max_length = 250, blank = True, help_text = "Escriba el enlace a Google Meet")
        enlaceYouTube = models.URLField(max_length = 250, blank = True, help_text = "Escriba el enlace a YouTube")
        ocultar_programa = models.BooleanField('No mostrar', default = False)
        class Meta:
                verbose_name_plural = 'Programas'
                ordering = ['id']
        def __str__(self):
                return self.nombre