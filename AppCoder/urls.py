from django.urls import path
from AppCoder.views import other , usuarios
from AppCoder.views.Clientes import leerClientes, eliminarClientes, editarClientes, form_clientes
from AppCoder.views.operarios import form_operario 
from AppCoder.views.unidades import form_unidades, leerUnidades, editarUnidad, eliminarUnidad
from AppCoder.views.ordenes import form_orden_trabajo, leer_ordenes_trabajo, editar_orden_trabajo, eliminar_orden_trabajo, marcar_entregado
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy 
from django.contrib.auth.views import LogoutView

urlpatterns =[
    # Páginas principales

    path('clientes/', leerClientes, name='leerClientes'),
    path('operario/', other.operario, name='operario'),
    path('unidades/', leerUnidades, name='unidades'),
    
    # Formularios
    
    path('form_operario/', form_operario, name='form_operario'),
    path('form_unidades/', form_unidades, name='form_unidades'),
    
    path('ordenes_trabajo/', leer_ordenes_trabajo, name='ordenes_trabajo'),

    # Búsquedas
    path('buscar_clientes/', other.buscar_clientes, name='buscar_clientes'),
    path('buscar_unidades/', other.buscar_unidades, name='buscar_unidades'),
    path('', other.inicio, name='inicio'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # CRUD Clientes
    path('clientes/crear/', form_clientes, name='crear_cliente'),
    path('clientes/<int:id_cliente>/editar/', editarClientes, name='editarClientes'),
    path('clientes/<int:id_cliente>/eliminar/', eliminarClientes, name='eliminarClientes'),
    path('editar_unidad/<int:id_unidad>/', editarUnidad, name='editar_unidad'),
    path('eliminar_unidad/<int:id_unidad>/', eliminarUnidad, name='eliminar_unidad'),
    path('form_orden_trabajo/', form_orden_trabajo, name='form_orden_trabajo'),
    path('ordenes_trabajo/editar/<int:id_orden>/', editar_orden_trabajo, name='editar_orden_trabajo'),
    path('ordenes_trabajo/eliminar/<int:id_orden>/', eliminar_orden_trabajo, name='eliminar_orden_trabajo'),
    path('orden_trabajo/<int:orden_id>/marcar_entregado/', marcar_entregado, name='marcar_entregado'),
    path('login/', auth_views.LoginView.as_view(template_name='AppCoder/login.html'), name='login'),
    path('usuarios/', usuarios.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', usuarios.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', usuarios.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', usuarios.eliminar_usuario, name='eliminar_usuario'),
]

