from django.forms import ModelForm
from .models import Contacto_Model



class ContactoForm(ModelForm):
    class Meta:
        contactos = Contacto_Model()
        fields = '__all__'
        exclude = ['id']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono1': 'Telefono1',
            'telefono2': 'Telefono2',
            'compañia': 'Compañia',
            'fecha_creacion': 'Fecha de creacion'
        }
        
    
    