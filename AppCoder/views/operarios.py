from django.shortcuts import render, redirect
from AppCoder.forms import OperarioFormulario
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def form_operario(request):
    if request.method == 'POST':
        form = OperarioFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operario creado exitosamente')
            return redirect('form_operario')
    else:
        form = OperarioFormulario()
    return render(request, "AppCoder/formularios/form_operario.html", {'form': form})

