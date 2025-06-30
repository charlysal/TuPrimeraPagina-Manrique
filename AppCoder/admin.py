from django.contrib import admin
from .models import Clientes, Operario, Unidades, Entregas

admin.site.register(Clientes)
admin.site.register(Operario)
admin.site.register(Unidades)
admin.site.register(Entregas)
