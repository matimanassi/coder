from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, EditorialForm
from .models import Autor, Libro, Editorial

def home(request):
    return render(request, 'inicio/index.html')

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'inicio/agregar_autor.html', {'form': form})

def buscar_libro(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Libro.objects.filter(titulo__icontains=query)
    return render(request, 'inicio/buscar_libro.html', {'resultados': resultados, 'query': query})