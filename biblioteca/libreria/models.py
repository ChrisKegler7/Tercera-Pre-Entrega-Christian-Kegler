from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Review(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.usuario} - {self.libro}"
