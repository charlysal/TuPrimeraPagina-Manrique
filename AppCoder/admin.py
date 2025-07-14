from django.contrib import admin
from .models import Clientes, Operario, Unidades
from .models import Accesorio

admin.site.register(Accesorio)
admin.site.register(Clientes)
admin.site.register(Operario)
admin.site.register(Unidades)
