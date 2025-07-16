from AppCoder.views.personal_autorizado import listar_personal, crear_personal, editar_personal, eliminar_personal
from django.urls import path
from AppCoder.views.editar_avatar import editar_avatar
from AppCoder.views import other, usuarios
from AppCoder.views.Clientes import leerClientes, eliminarClientes, editarClientes, form_clientes, detalleCliente
from AppCoder.views.operarios import form_operario
from AppCoder.views.unidades import form_unidades, leerUnidades, editarUnidad, eliminarUnidad
from AppCoder.views.ordenes import form_orden_trabajo, leer_ordenes_trabajo, editar_orden_trabajo, eliminar_orden_trabajo, marcar_entregado
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # CRUD Personal Autorizado
    path('personal/', listar_personal, name='listar_personal'),
    path('personal/crear/', crear_personal, name='crear_personal'),
    path('personal/editar/<int:pk>/', editar_personal, name='editar_personal'),
    path('personal/eliminar/<int:pk>/', eliminar_personal, name='eliminar_personal'),
    path('', other.inicio, name='inicio'),

    # About ME page
    path('about_me/', other.about_me, name='about_me'),

    # CRUD Clientes (protegido)
    path('clientes/', leerClientes, name='leerClientes'),
    path('clientes/crear/', form_clientes, name='crear_cliente'),
    path('clientes/<int:id_cliente>/', detalleCliente, name='detalleCliente'),
    path('clientes/<int:id_cliente>/editar/', editarClientes, name='editarClientes'),
    path('clientes/<int:id_cliente>/eliminar/', eliminarClientes, name='eliminarClientes'),

    # CRUD Unidades (protegido)
    path('unidades/', leerUnidades, name='unidades'),
    path('form_unidades/', form_unidades, name='form_unidades'),
    path('editar_unidad/<int:id_unidad>/', editarUnidad, name='editar_unidad'),
    path('eliminar_unidad/<int:id_unidad>/', eliminarUnidad, name='eliminar_unidad'),

    # CRUD Ordenes (protegido)
    path('ordenes_trabajo/', leer_ordenes_trabajo, name='ordenes_trabajo'),
    path('form_orden_trabajo/', form_orden_trabajo, name='form_orden_trabajo'),
    path('ordenes_trabajo/editar/<int:id_orden>/', editar_orden_trabajo, name='editar_orden_trabajo'),
    path('ordenes_trabajo/eliminar/<int:id_orden>/', eliminar_orden_trabajo, name='eliminar_orden_trabajo'),
    path('orden_trabajo/<int:orden_id>/marcar_entregado/', marcar_entregado, name='marcar_entregado'),

    # CRUD Operarios (protegido)
    path('form_operario/', form_operario, name='form_operario'),

    # CRUD Usuarios (protegido)
    path('usuarios/', usuarios.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', usuarios.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', usuarios.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', usuarios.eliminar_usuario, name='eliminar_usuario'),

    # Avatar usuario
    path('editar_avatar/', editar_avatar, name='editar_avatar'),
    # Login/Logout
    path('login/', auth_views.LoginView.as_view(template_name='AppCoder/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]