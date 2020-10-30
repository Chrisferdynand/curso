from django.contrib import admin
from course.models import *
# Register your models here.
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tema', 'FechaHora', 'enlaceMeet', 'enlaceYouTube', 'ocultar_programa')
    list_filter = ['id']
    search_fields = ['nombre']
admin.site.register(Programa, ProgramaAdmin)