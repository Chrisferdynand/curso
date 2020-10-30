from django.shortcuts import render
from course.models import *
# Create your views here.
def programas(request):
	entradas = Programa.objects.all().exclude(ocultar_programa = True)
	return render(request, 'programa.html', {'entradas':entradas})