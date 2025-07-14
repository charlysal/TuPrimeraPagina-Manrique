from django import forms
from .models import Operario, Clientes, Unidades, OrdenDeTrabajo, Accesorio


class OperarioFormulario(forms.ModelForm):
    class Meta:
        model = Operario
        fields = ['nombre', 'apellido', 'legajo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'legajo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ClientesFormulario(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'email']

class UnidadesFormulario(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = ['cliente', 'modelo', 'chasis']


class AccesorioFormulario(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['nombre']

class OrdenDeTrabajoFormulario(forms.ModelForm):
    class Meta:
        model = OrdenDeTrabajo
        fields = [
            'unidad',
            'descripcion',
            'accesorios_instalados',
            'instalador',
            'sucursal',
            'nombre_empleado_entrego',
            'confirmacion_entregado',  
        ]


