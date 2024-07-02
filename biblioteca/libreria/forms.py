from django import forms
from .models import *

class CustomDateInput(forms.DateInput):
    input_type = 'text'

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'isbn']
        widgets = {
            'fecha_publicacion': CustomDateInput(),
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': CustomDateInput(),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'direccion']

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ['libro', 'usuario', 'comentario', 'calificacion']

