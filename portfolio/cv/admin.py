from django.contrib import admin
from .models import Formacion, Blog, Proyecto

# Registro de modelos
admin.site.register(Proyecto)
admin.site.register(Formacion)
admin.site.register(Blog)

#Añadimos el nombre personalizado del admin
admin.site.site_header='PortFolio AmggDeveloper'
admin.site.site_title='amggDeveloper'
admin.site.index_title = 'PortFolio'
