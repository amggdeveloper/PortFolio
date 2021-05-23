#portfolio URL Configuration
from django.contrib import admin
from django.urls import path, include
from cv import views
from django.conf import settings
from django.conf.urls.static import static

#Rutas
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),#ruta para utilizar la plantilla jet en el admin
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),#ruta panel de control color django-jet
    path('',views.home, name="home"),#ruta a la página de inicio   
    path('formacion/',views.cv, name="cv"),#ruta a la página de cv
    path('blog/',views.blog, name="blog"),#ruta a la página del blog
    path('contacto/',views.contact, name="contact"),#ruta a la página de contacto
    path('admin/', admin.site.urls),#ruta a la página de administración    
]

#Enlace con la carpeta static en el modo DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)