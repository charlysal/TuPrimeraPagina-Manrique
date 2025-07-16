from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from AppCoder.forms import ClientesFormulario
from AppCoder.models import Clientes
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def eliminarClientes(request, id_cliente):
    cliente = get_object_or_404(Clientes, id=id_cliente)

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, f"Cliente {cliente.nombre} eliminado correctamente.")
        return redirect('leerClientes')

    return render(request, "AppCoder/formularios/eliminarclientes.html", {"cliente": cliente})

@login_required
def leerClientes(request):
    """Leer todos los clientes"""
    clientes = Clientes.objects.all().order_by('-id')

    
    return render(request, "AppCoder/formularios/leerclientes.html", {"clientes": clientes})


@login_required
def detalleCliente(request, id_cliente):
    cliente = get_object_or_404(Clientes, id=id_cliente)
    return render(request, "AppCoder/formularios/detalle_cliente.html", {"cliente": cliente})


@login_required
def editarClientes(request, id_cliente):
    cliente = get_object_or_404(Clientes, id=id_cliente)

    if request.method == 'POST':
        miFormulario = ClientesFormulario(request.POST)
        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.email = informacion['email']
            cliente.save()
            messages.success(request, 'Cliente actualizado exitosamente')
            return redirect('leerClientes')  
    else:
        miFormulario = ClientesFormulario(
            initial={
                'nombre': cliente.nombre,
                'apellido': cliente.apellido,
                'email': cliente.email,
            }
        )
    
    return render(request, "AppCoder/formularios/editarClientes.html", 
                  {"miFormulario": miFormulario, "cliente_id": cliente.id})

@login_required
def form_clientes(request):
    """Formulario para crear nuevos clientes"""
    if request.method == 'POST':
        form = ClientesFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente')
            return redirect('leerClientes')  
    else:
        form = ClientesFormulario()
    return render(request, "AppCoder/formularios/form_clientes.html", {'form': form})



