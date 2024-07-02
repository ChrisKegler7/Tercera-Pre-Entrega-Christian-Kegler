from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.core.exceptions import PermissionDenied


def home(request):
    libros = []
    context = {"libros": libros}
    return render(request, 'libreria/home.html', context)

def index(request):
    return render(request, 'libreria/index.html')

def buscar_libro_view(request):
    libros = []
    if 'q' in request.GET:
        query = request.GET['q']
        libros = Libro.objects.filter(titulo__icontains=query)
    return render(request, 'libreria/buscar_libro.html', {'libros': libros})

def lista_libros(request):
    libros = Libro.objects.all()
    context = {
        'libros': libros
    }
    return render(request, 'libreria/lista_libros', context)

def is_admin(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True

def agregar_autor_libro(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST, prefix='autor')
        libro_form = LibroForm(request.POST, prefix='libro')
        
        if autor_form.is_valid() and libro_form.is_valid():
            autor = autor_form.save()
            libro = libro_form.save(commit=False)
            libro.autor = autor
            libro.save()
            return redirect('home')
    else:
        autor_form = AutorForm(prefix='autor')
        libro_form = LibroForm(prefix='libro')
    
    return render(request, 'libreria/agregar_autor_libro.html', {
        'autor_form': autor_form,
        'libro_form': libro_form,
    })

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libreria:agregar_cliente')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()

    return render(request, 'libreria/agregar_cliente.html', {'form': form, 'clientes': clientes})


def reviews(request):
    reviews = Review.objects.all()
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libreria/reviews.html')
    else:
        form = ReviewsForm()
    return render(request, 'libreria/reviews.html', {'form': form, 'reviews': reviews})

