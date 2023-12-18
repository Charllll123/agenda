from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('contactos/', include('contactos.urls'), name = 'contactos'),
    path('tareas/', include('tareas.urls'), name = 'tareas'),
    
]
