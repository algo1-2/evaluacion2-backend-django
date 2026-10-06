# Portal de Películas - Django

Proyecto desarrollado para la asignatura de **Programación Back End** en **INACAP**.

---

## Integrante

* **Nombre:** Benjamín Rivas
* **Correo Institucional:** [benjamin.rivas10@inacapmail.cl](mailto:benjamin.rivas10@inacapmail.cl)
* **Asignatura:** Programación Back End

---

## Descripción del Proyecto

Aplicación web desarrollada con el framework **Django** y estilizada con **Bootstrap 5**. Permite navegar por un catálogo de películas agrupadas en dos géneros cinematográficos: **Ciencia Ficción** y **Animación**.

### Características principales:
* Estructura modular basada en plantillas (`base.html`, `inicio.html`, `genero.html`).
* Envío de datos estructurados desde las vistas hacia los templates utilizando condicionales y bucles.
* Catálogo detallado por película con título, año de estreno, director, clasificación por edad, sinopsis e imágenes estáticas.
* Navegación organizada con rutas amigables y namespaces (`home:inicio` y `home:genero`).
* Diseño responsivo para dispositivos móviles y escritorio.

---

## Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/algo1-2/evaluacion2-backend-django.git
cd evaluacion2-backend-django
```

### 2. Crear y activar el entorno virtual
En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre tu navegador e ingresa a: **http://127.0.0.1:8000/**
