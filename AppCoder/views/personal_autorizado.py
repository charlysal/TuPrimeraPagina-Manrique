from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from AppCoder.models import PersonalAutorizado
from AppCoder.forms import PersonalAutorizadoForm
from django.contrib import messages

@login_required
def listar_personal(request):
    personal = PersonalAutorizado.objects.select_related('user').all()
    return render(request, 'AppCoder/personal_autorizado/listar.html', {'personal': personal})

@login_required
def crear_personal(request):
    if request.method == 'POST':
        form = PersonalAutorizadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Personal autorizado creado exitosamente.")
            return redirect('listar_personal')
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = PersonalAutorizadoForm()
    return render(request, 'AppCoder/personal_autorizado/crear.html', {'form': form})

@login_required
def editar_personal(request, pk):
    persona = get_object_or_404(PersonalAutorizado, pk=pk)
    if request.method == 'POST':
        form = PersonalAutorizadoForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, "Personal autorizado actualizado exitosamente.")
            return redirect('listar_personal')
        else:
            messages.error(request, "Corrige los errores del formulario.")
    else:
        form = PersonalAutorizadoForm(instance=persona)
    return render(request, 'AppCoder/personal_autorizado/editar.html', {'form': form, 'persona': persona})

@login_required
def eliminar_personal(request, pk):
    persona = get_object_or_404(PersonalAutorizado, pk=pk)
    if request.method == 'POST':
        persona.delete()
        messages.success(request, "Personal autorizado eliminado exitosamente.")
        return redirect('listar_personal')
    return render(request, 'AppCoder/personal_autorizado/eliminar.html', {'persona': persona})
