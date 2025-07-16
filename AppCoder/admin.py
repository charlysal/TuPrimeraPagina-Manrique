from django.contrib import admin

from .models import Clientes, Operario, Unidades, Accesorio, PersonalAutorizado

admin.site.register(Accesorio)
admin.site.register(Clientes)
admin.site.register(Operario)
admin.site.register(Unidades)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PersonalAutorizadoInline(admin.StackedInline):
    model = PersonalAutorizado
    can_delete = False
    verbose_name_plural = 'Personal Autorizado'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (PersonalAutorizadoInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_select_related = ('personautorizado',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(PersonalAutorizado)
class PersonalAutorizadoAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'activo', 'telefono')
    list_filter = ('activo', 'cargo')
    search_fields = ('user__username', 'cargo', 'telefono')
    actions = ['marcar_inactivo']

    def marcar_inactivo(self, request, queryset):
        queryset.update(activo=False)
        self.message_user(request, "Personal marcado como inactivo.")
    marcar_inactivo.short_description = "Marcar como inactivo"
