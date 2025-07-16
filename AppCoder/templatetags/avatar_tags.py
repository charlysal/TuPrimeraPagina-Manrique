from AppCoder.models import Perfil

def avatar(request):
    if request.user.is_authenticated:
        try:
            perfil = Perfil.objects.get(user=request.user)
        except Perfil.DoesNotExist:
            perfil = None
        return {'avatar': perfil.imagen.url if perfil and perfil.imagen else None}
    return {'avatar': None}
