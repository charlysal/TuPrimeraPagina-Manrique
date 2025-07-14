from django import forms 
from .models import Operario, Clientes, Unidades, OrdenDeTrabajo, Accesorio
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




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


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("El correo electrónico es obligatorio.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo electrónico.")
        return email
