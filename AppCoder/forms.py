
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, PersonalAutorizado, Operario, Clientes, Unidades, OrdenDeTrabajo, Accesorio

# Formulario para subir/editar avatar de usuario
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen']
        labels = {'imagen': 'Foto de perfil'}
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }



# Formulario combinado para crear usuario y personal autorizado
class PersonalAutorizadoForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Nombre", max_length=30, required=False)
    last_name = forms.CharField(label="Apellido", max_length=30, required=False)
    email = forms.EmailField(label="Correo electrónico", required=False)

    class Meta:
        model = PersonalAutorizado
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'cargo', 'activo', 'telefono', 'observaciones']
        widgets = {
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        # Si se pasa instancia, rellenar campos de usuario
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {})
        if instance:
            initial['username'] = instance.user.username
            initial['first_name'] = instance.user.first_name
            initial['last_name'] = instance.user.last_name
            initial['email'] = instance.user.email
            kwargs['initial'] = initial
        super().__init__(*args, **kwargs)
        # Si es edición, no requerir contraseña
        if instance:
            self.fields['password1'].required = False
            self.fields['password2'].required = False
        else:
            self.fields['password1'].required = True
            self.fields['password2'].required = True

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if self.instance and not password1 and not password2:
            # No cambio de contraseña
            return cleaned_data
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if not password1:
            raise forms.ValidationError("La contraseña es obligatoria.")
        return cleaned_data

    def save(self, commit=True):
        # Crear o actualizar usuario
        from django.contrib.auth.models import User
        data = self.cleaned_data
        if self.instance and hasattr(self.instance, 'user') and self.instance.user_id:
            user = self.instance.user
            user.username = data['username']
            user.first_name = data.get('first_name', '')
            user.last_name = data.get('last_name', '')
            user.email = data.get('email', '')
            if data.get('password1'):
                user.set_password(data['password1'])
            if commit:
                user.save()
            personal = super().save(commit=False)
            personal.user = user
            if commit:
                personal.save()
            return personal
        else:
            user = User.objects.create_user(
                username=data['username'],
                password=data['password1'],
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                email=data.get('email', '')
            )
            personal = super().save(commit=False)
            personal.user = user
            if commit:
                personal.save()
            return personal




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
        widgets = {
            'accesorios_instalados': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Detalle los accesorios instalados'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'sucursal': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_empleado_entrego': forms.TextInput(attrs={'class': 'form-control'}),
        }


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
