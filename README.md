# Proyecto Django MVT

Este proyecto incluye una aplicación web construida con el patrón MVT (Modelo-Vista-Template) utilizando Django.

## Requisitos

- Python 3.x
- Django
- Otros paquetes especificados en `requirements.txt`

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd mi_proyecto_django
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows, usar `env\Scripts\activate`
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar migraciones y servidor de desarrollo:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Visitar `http://127.0.0.1:8000/` en el navegador.

## Funcionalidades

- **Herencia de HTML**: La plantilla `base.html` es heredada por otras plantillas.
- **Modelos**: Tres modelos (`Autor`, `Libro`, `Editorial`) con relaciones.
- **Formularios**: Formularios para agregar autores y buscar libros.
- **Búsqueda**: Formulario de búsqueda de libros en la base de datos.

## Pruebas

1. **Agregar Autor**: Visitar `/agregar_autor/` y agregar un nuevo autor.
2. **Buscar Libro**: Visitar `/buscar_libro/` y buscar un libro por su título.