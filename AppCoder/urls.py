from django.urls import path
from AppCoder.views import other
from AppCoder.views.Clientes import leerClientes, eliminarClientes, editarClientes, form_clientes
from AppCoder.views.operarios import form_operario
from AppCoder.views.unidades import form_unidades, leerUnidades, editarUnidad, eliminarUnidad
from AppCoder.views.ordenes import form_orden_trabajo, leer_ordenes_trabajo, editar_orden_trabajo, eliminar_orden_trabajo, marcar_entregado


urlpatterns = [
    # Páginas principales
    path('', other.inicio, name='inicio'),
    path('clientes/', other.clientes, name='clientes'),
    path('operario/', other.operario, name='operario'),
    # path('unidades/', other.unidades, name='unidades'),  
    path('unidades/', leerUnidades, name='unidades'),
    #path('entregas/', other.entregas, name='entregas'),

    # Formularios
    # path('form_clientes/', form_clientes, name='form_clientes'),
    path('form_operario/', form_operario, name='form_operario'),
    path('form_unidades/', form_unidades, name='form_unidades'),
    #path('form_entregas/', form_entregas, name='form_entregas'),
    path('ordenes_trabajo/', leer_ordenes_trabajo, name='ordenes_trabajo'),


    # Búsquedas
    path('buscar_clientes/', other.buscar_clientes, name='buscar_clientes'),
    path('buscar_unidades/', other.buscar_unidades, name='buscar_unidades'),

    # CRUD Clientes
    path('leerClientes/', leerClientes, name='leerClientes'),
    path('clientes/crear/', form_clientes, name='crear_cliente'),
    path('eliminarCliente/<int:id_cliente>/', eliminarClientes, name='eliminarClientes'),
    path('editarCliente/<int:id_cliente>/', editarClientes, name='editarClientes'),
    path('editar_unidad/<int:id_unidad>/', editarUnidad, name='editar_unidad'),
    path('eliminar_unidad/<int:id_unidad>/', eliminarUnidad, name='eliminar_unidad'),
    path('form_orden_trabajo/', form_orden_trabajo, name='form_orden_trabajo'),
    path('ordenes_trabajo/editar/<int:id_orden>/', editar_orden_trabajo, name='editar_orden_trabajo'),
    path('ordenes_trabajo/eliminar/<int:id_orden>/', eliminar_orden_trabajo, name='eliminar_orden_trabajo'),
    #path('ordenes/marcar_entregado/<int:orden_id>/', marcar_entregado, name='marcar_entregado'),
    path('orden_trabajo/<int:orden_id>/marcar_entregado/', marcar_entregado, name='marcar_entregado'),


]

