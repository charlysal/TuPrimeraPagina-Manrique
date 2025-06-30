from django import forms
from .models import Operario, Clientes, Unidades, Entregas

class OperarioFormulario(forms.ModelForm):
    class Meta:
        model = Operario
        fields = ['instalador', 'OrdenDeTrabajo']

class ClientesFormulario(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre', 'apellido', 'email']

class UnidadesFormulario(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = ['modelo', 'chasis', 'accesorios']

class EntregasFormulario(forms.ModelForm):
    class Meta:
        model = Entregas
        fields = ['sucursal', 'nombre', 'fechaDeEntrega', 'entregado']

