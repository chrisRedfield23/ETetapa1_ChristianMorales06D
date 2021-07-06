from django import forms 
from django.forms import ModelForm, widgets
from .models import colaboradores


class colaboForm(ModelForm):
    
    class Meta:
        model=colaboradores
        fields = ['rut', 'foto', 'nombre', 'apellido','telefono','direccion','correo_electronico', 'pais','contrasena']
        labels ={
            'rut':'Ingrese rut',
            'foto': 'Ingrese foto del proveedor',
            'nombre': 'Ingrese nombre',
            'apellido': 'ingrese apellido',
            'telefono':'Ingrese número telefónico',
            'dirección':'dirección',
            'correo_electronico':'Ingrese correo electronico',
            'pais':'País',
            'contrasena':'Ingrese contrasena',

        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'rut',
                    'id': 'rut'
                }
            ),
            'foto':forms.ClearableFileInput( 
                   attrs={
                  'class':'form-control' 

                  
                }
            ),

            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'nombre',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'apellido',
                    'id': 'apellido'
                }
            ),
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'telefono',
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                     'placeholder':'direccion',
                    'id': 'direccion'
                }
            ),
            'correo_electronico': forms.TextInput(
                attrs={
                    'class': 'form-control',
                     'placeholder':'correo_electronico',
                    'id': 'correo_electronico'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                     'placeholder':'pais',
                    'id': 'pais'
                }
            ),
            'contrasena': forms.TextInput(
                attrs={
                    'class': 'form-control',
                     'placeholder':'contrasena',
                    'id': 'contrasena'
                }
            ),
                

        }