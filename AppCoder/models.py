from django.db import models


class Operario(models.Model):
    instalador = models.CharField(max_length=100)  # Campo string de 100 caracteres
    OrdenDeTrabajo = models.IntegerField()  # Campo entero

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)  
    apellido = models.CharField(max_length=30)  
    email = models.EmailField()  # Campo de email

class Unidades(models.Model):
    modelo = models.CharField(max_length=30)  
    chasis = models.CharField(max_length=30)  
    accesorios = models.CharField(max_length=100)
    

class Entregas(models.Model):
    sucursal = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    fechaDeEntrega = models.DateField()  # Campo de fecha
    entregado = models.BooleanField()  # Campo booleano
