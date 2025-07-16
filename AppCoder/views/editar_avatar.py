from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppCoder.forms import AvatarForm
from AppCoder.models import Perfil

@login_required
def editar_avatar(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AvatarForm(instance=perfil)
    return render(request, 'AppCoder/editar_avatar.html', {'form': form, 'perfil': perfil})
