from django.shortcuts import render, redirect , get_object_or_404
from AppCoder.forms import OrdenDeTrabajoFormulario
from django.contrib import messages
from AppCoder.models import OrdenDeTrabajo


def form_orden_trabajo(request):
    if request.method == 'POST':
        form = OrdenDeTrabajoFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Orden de trabajo creada correctamente.")
            return redirect('ordenes_trabajo') 
    else:
        form = OrdenDeTrabajoFormulario()
    
    return render(request, "AppCoder/formularios/form_orden_trabajo.html", {"form": form})

def leer_ordenes_trabajo(request):
    ordenes = OrdenDeTrabajo.objects.all().order_by('-id')  # orden descendente (más recientes primero)
    return render(request, "AppCoder/formularios/leer_ordenes_trabajo.html", {"ordenes": ordenes})

def editar_orden_trabajo(request, id_orden):
    orden = get_object_or_404(OrdenDeTrabajo, id=id_orden)

    if request.method == 'POST':
        form = OrdenDeTrabajoFormulario(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            messages.success(request, "Orden de trabajo actualizada exitosamente.")
            return redirect('ordenes_trabajo')
    else:
        form = OrdenDeTrabajoFormulario(instance=orden)

    return render(request, "AppCoder/formularios/editar_orden_trabajo.html", {"form": form, "orden": orden})


# ELIMINAR
def eliminar_orden_trabajo(request, id_orden):
    orden = get_object_or_404(OrdenDeTrabajo, id=id_orden)

    if request.method == 'POST':
        orden.delete()
        messages.success(request, "Orden de trabajo eliminada correctamente.")
        return redirect('ordenes_trabajo')

    return render(request, "AppCoder/formularios/eliminar_orden_trabajo.html", {"orden": orden})


def marcar_entregado(request, orden_id):
    orden = get_object_or_404(OrdenDeTrabajo, id=orden_id)
    orden.confirmacion_entregado = True
    orden.save()
    return redirect('ordenes_trabajo')
