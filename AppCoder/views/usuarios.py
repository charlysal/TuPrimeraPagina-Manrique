from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from AppCoder.forms import UserEditForm, CustomUserCreationForm

@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'AppCoder/usuarios/listar.html', {'usuarios': usuarios})

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = CustomUserCreationForm()
    return render(request, 'AppCoder/usuarios/crear.html', {'form': form})

@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'AppCoder/usuarios/editar.html', {'form': form})

@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'AppCoder/usuarios/eliminar.html', {'usuario': usuario})


