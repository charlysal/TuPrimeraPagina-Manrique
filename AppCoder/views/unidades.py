from django.shortcuts import render, redirect , get_object_or_404
from AppCoder.forms import UnidadesFormulario
from django.contrib import messages
from AppCoder.models import Unidades 


def leerUnidades(request):
    unidades = Unidades.objects.all().order_by('-id').prefetch_related('ordenes')
    unidades_con_ordenes = {u.id: u.ordenes.all() for u in unidades if u.ordenes.exists()}
    contexto = {
        'unidades': unidades,
        'unidades_con_ordenes': unidades_con_ordenes,
    }
    return render(request, 'AppCoder/leer_unidades.html', contexto)
    
def form_unidades(request):
    if request.method == 'POST':
        form = UnidadesFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_unidades') 
    else:
        form = UnidadesFormulario()

    unidades = Unidades.objects.all().order_by('-id').select_related('cliente')

    contexto = {
        'form': form,
        'unidades': unidades,
    }

    return render(request, 'AppCoder/formularios/form_unidades.html', contexto)




def editarUnidad(request, id_unidad):
    unidad = get_object_or_404(Unidades, id=id_unidad)

    if request.method == 'POST':
        form = UnidadesFormulario(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidad actualizada correctamente.")
            return redirect('unidades')
    else:
        form = UnidadesFormulario(instance=unidad)

    return render(request, "AppCoder/formularios/editar_unidad.html", {
        "form": form,
        "unidad": unidad
    })

def eliminarUnidad(request, id_unidad):
    unidad = get_object_or_404(Unidades, id=id_unidad)

    if request.method == 'POST':
        unidad.delete()
        messages.success(request, "Unidad eliminada correctamente.")
        return redirect('unidades')

    return render(request, "AppCoder/formularios/eliminar_unidad.html", {
        "unidad": unidad
    })
