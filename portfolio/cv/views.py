from django.shortcuts import render, get_object_or_404
from .models import Proyecto
from .models import Formacion
from .models import Blog

# Creamos nuestras Vistas aquí
def home(request):
    proyectos=Proyecto.objects.all()
    return render(request,'index.html',{'proyectos':proyectos})#Página de Proyectos
def cv(request):
    cv=Formacion.objects.all()
    return render(request,'cv.html',{'cv':cv})#Página de Formación
def blog(request):
    blog=Blog.objects.all()
    return render(request,'blog.html',{'blog':blog})#Página del Blog
def contact(request):
    return render(request,'contact.html',{'contacto':contact})#Página de Contacto                 


