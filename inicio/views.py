from django.shortcuts import render, redirect, get_object_or_404
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

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'inicio/listar_autores.html', {'autores': autores})

def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'inicio/editar_autor.html', {'form': form, 'autor': autor})

def borrar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'inicio/borrar_autor.html', {'autor': autor})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm()
    return render(request, 'inicio/agregar_libro.html', {'form': form})

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'inicio/listar_libros.html', {'libros': libros})

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'inicio/editar_libro.html', {'form': form, 'libro': libro})

def borrar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'inicio/borrar_libro.html', {'libro': libro})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditorialForm()
    return render(request, 'inicio/agregar_editorial.html', {'form': form})

def listar_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'inicio/listar_editoriales.html', {'editoriales': editoriales})

def editar_editorial(request, editorial_id):
    editorial = get_object_or_404(Editorial, id=editorial_id)
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('listar_editoriales')
    else:
        form = EditorialForm(instance=editorial)
    return render(request, 'inicio/editar_editorial.html', {'form': form, 'editorial': editorial})

def borrar_editorial(request, editorial_id):
    editorial = get_object_or_404(Editorial, id=editorial_id)
    if request.method == 'POST':
        editorial.delete()
        return redirect('listar_editoriales')
    return render(request, 'inicio/borrar_editorial.html', {'editorial': editorial})