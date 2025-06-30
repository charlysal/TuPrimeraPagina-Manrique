from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('operario/', views.operario, name='operario'),
    path('unidades/', views.unidades, name='unidades'),
    path('entregas/', views.entregas, name='entregas'),

    # Formularios
    path('form_clientes/', views.form_clientes, name='form_clientes'),
    path('form_operario/', views.form_operario, name='form_operario'),
    path('form_unidades/', views.form_unidades, name='form_unidades'),
    path('form_entregas/', views.form_entregas, name='form_entregas'),
    path('buscar_clientes/', views.buscar_clientes, name='buscar_clientes'), 
    path('buscar_unidades/', views.buscar_unidades, name='buscar_unidades'),
]
