from django.db import models #importamos tablas de la bd
from django.utils import timezone #importamos función fecha-hora
from django.contrib.auth.models import User #importamos user

# Creación de los modelos
#Creamos la clase para proyectos, donde se añadiran los proyectos creados
class Proyecto(models.Model):

    fecha=models.CharField(max_length=150) #creamos un cuadro para la fecha del proyecto
    titulo=models.CharField(max_length=150) #Creamos un cuadro de texto para insertar el titulo del proyecto con un máximo
    descripcion=models.TextField(max_length=150) #Creamos un cuadro de texto para poner la descripción del proyecto
    video=models.URLField() #Creamos un campo para añadir la url de los videos

    #Ordenamos los proyectos por fecha
    class Meta:   #Creamos la clase metadatos
        ordering = ('-fecha',) #Ordena por fecha descendente (primero los actuales)

    #Recogemos el titulo del proyecto para hacer la lista
    def __str__(self): #función que devuelve el titulo
        return self.titulo 

#creamos la clase formacion, donde se añadirán todos los datos relacionados con la formación
class Formacion(models.Model):
    
    #Creamos los cuadro de texto y los seleccionables para añadir los datos al CV   
    fecha=models.DateField(default=timezone.now) #Fecha finalización formación
    titulo=models.CharField(max_length=150)#cuadro de texto para el titulo, con máximo de carácteres
    texto=models.TextField()#cuadro de texto para añadir la descripción   
       
    #Recogemos el titulo de la formación para la lista 
    def __str__(self): #función que devuelve el titulo
        return self.titulo 
    #Recogemos solo el año de la fecha para la formación
    def anioFormacion(self):
        return self.fecha.strftime('%Y')
    #Ordenamos la formación por fecha
    class Meta:   #Creamos la clase metadatos
        ordering = ('-fecha',) #Ordena por fecha descendente (primero los actuales)

#creamos la clase Blog, en donde se añadirán todos las entradas del blog
class Blog(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)#autor de la entrada en el blog
    titulo = models.CharField(max_length=200)#titulo de la entrada en el blog
    texto = models.TextField() #texto del blog
    imagen=models.ImageField(null=True, upload_to='img') #Seleccionador de imagenes
    fecha_creacion = models.DateTimeField( #fecha de creación
            default=timezone.now)
    fecha_publicacion = models.DateTimeField( #fecha de publicación
            blank=True, null=True)

    #publicado
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #Recogemos el titulo de la entrada para la lista
    def __str__(self):#función que devuelve el titulo
        return self.titulo