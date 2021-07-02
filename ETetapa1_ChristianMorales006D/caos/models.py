from django.db import models

# Create your models here.

class colaboradores(models.Model):
    rut = models.CharField(max_length=40,primary_key=True, verbose_name='rut: ')
    foto=models.ImageField(upload_to='img/', null=True, blank=True)
    nombre  = models.CharField(max_length=20, verbose_name='nombre')
    apellido = models.CharField(max_length=20, verbose_name='apellido')
    telefono  = models.IntegerField(verbose_name='telefono')
    direccion = models.CharField(max_length=50, verbose_name='direccion')
    correo_electronico = models.CharField(max_length=40, verbose_name='correo_electronico')
    pais  = models.CharField(max_length=15, verbose_name='pais')
    contrasena = models.CharField(max_length=20, verbose_name='contrasena')

    def _str_(self):
        return(self.rut)