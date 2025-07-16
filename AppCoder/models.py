from django.db import models
from django.contrib.auth.models import User

class Operario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    legajo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} (Legajo: {self.legajo})"


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)  
    apellido = models.CharField(max_length=30)  
    email = models.EmailField()  # Campo de email
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email}"

class Unidades(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='unidades')
    modelo = models.CharField(max_length=30)
    chasis = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.modelo} ({self.chasis}) - Cliente: {self.cliente.nombre} {self.cliente.apellido}"





# --- Accesorio antes de OrdenDeTrabajo ---
class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class OrdenDeTrabajo(models.Model):
    unidad = models.ForeignKey(Unidades, related_name='ordenes', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    accesorios_instalados = models.TextField(blank=True, help_text="Accesorios instalados (texto libre)")
    sucursal = models.CharField(max_length=100, default="sin valor asignado")
    nombre_empleado_entrego = models.CharField(max_length=100, default="sin valor asignado")
    confirmacion_entregado = models.BooleanField(default=False)
    instalador = models.ForeignKey(Operario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Orden #{self.id} - {self.unidad}"


class PersonalAutorizado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=100, help_text="Cargo o rol del personal autorizado")
    activo = models.BooleanField(default=True, help_text="¿El personal está activo?")
    telefono = models.CharField(max_length=30, blank=True, null=True, help_text="Teléfono de contacto")
    observaciones = models.TextField(blank=True, null=True, help_text="Notas internas")

    def __str__(self):
        return f"{self.user.username} ({self.cargo})"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
