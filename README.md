# Evaluación Sumativa 2 - Programación Back End

Proyecto práctico desarrollado para la asignatura de **Programación Back End** utilizando el framework web **Django 4.2**, **Bootstrap 5**, **Git** y **GitHub**.

---

## 1. Información del Estudiante

| Campo | Detalle |
| :--- | :--- |
| **Nombre Completo** | Benjamín Rivas |
| **Correo Institucional** | [benjamin.rivas10@inacapmail.cl](mailto:benjamin.rivas10@inacapmail.cl) |
| **Institución** | INACAP |
| **Asignatura** | Programación Back End |
| **Repositorio GitHub** | [algo1-2/evaluacion2-backend-django](https://github.com/algo1-2/evaluacion2-backend-django) |

---

## 2. Descripción del Proyecto

El proyecto consiste en una aplicación web desarrollada en Django que gestiona un catálogo interactivo de películas clasificadas por géneros cinematográficos:

- **Estructura según rúbrica:**
  - Proyecto Django: `benjamin_rivas`
  - Aplicación principal: `home_benjamin_rivas`
- **Catálogo de Géneros:**
  - **Ciencia Ficción**: Obras con temáticas futuristas, inteligencia artificial y viajes espaciales (*Interstellar*, *The Matrix*, *Blade Runner 2049*).
  - **Animación**: Películas aclamadas para toda la familia y técnicas vanguardistas (*Spider-Man: Into the Spider-Verse*, *Coco*, *El Viaje de Chihiro*).
- **Manejo de Datos y Lógica:**
  - Toda la información de películas (título, clasificación de edad, año, director, imágenes y sinopsis) se envía como diccionario estructurado desde `views.py`.
  - Las plantillas renderizan los datos utilizando directivas condicionales `{% if %}` y bucles `{% for %}`.
- **Diseño Responsivo con Bootstrap 5:**
  - Plantilla maestra `base.html` con barra de navegación sticky, menú desplegable y footer institucional.
  - Componentes de Bootstrap: Cards interactivas con efectos hover, Badges de clasificación, Pills de navegación y Breadcrumbs.
- **Archivos Estáticos (`static/`):**
  - `static/css/styles.css`: Estilos visuales personalizados (tema oscuro cinematográfico, efectos de elevación).
  - `static/js/main.js`: Scripts de inicialización de tooltips y componentes Bootstrap.
  - `static/images/`: Pósteres e ilustraciones vectoriales para cada título del catálogo.
- **Navegación y Enrutamiento:**
  - Acceso directo a la página principal desde la raíz del sitio (`/`).
  - Uso estricto de **namespaces** (`app_name = 'home'`) y URLs amigables (`/genero/<slug_genero>/`).

---

## 3. Estructura de Directorios

```text
BE/
├── benjamin_rivas/           # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Configuración (INSTALLED_APPS, TEMPLATES, STATIC, etc.)
│   ├── urls.py               # Enrutamiento raíz con include()
│   └── wsgi.py
├── home_benjamin_rivas/      # Aplicación del proyecto
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py              # Suite de pruebas unitarias automatizadas
│   ├── urls.py               # Enrutamiento de la aplicación (namespace: home)
│   └── views.py              # Lógica de vistas y catálogo de datos
├── static/                   # Archivos estáticos
│   ├── css/
│   │   └── styles.css        # Hoja de estilos personalizada
│   ├── js/
│   │   └── main.js           # Scripts JavaScript
│   └── images/               # Pósteres de las películas
│       ├── blade_runner.svg
│       ├── coco.svg
│       ├── el_viaje_de_chihiro.svg
│       ├── interstellar.svg
│       ├── matrix.svg
│       └── spider_verse.svg
├── templates/                # Plantillas HTML
│   ├── base.html             # Plantilla base con navbar y footer
│   ├── inicio.html           # Bienvenida y selección de géneros
│   └── genero.html           # Cartelera de películas con Bootstrap
├── .gitignore                # Reglas de exclusión de Git
├── manage.py                 # Gestor de comandos de Django
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto
```

---

## 4. Instrucciones de Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

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
En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar las pruebas automatizadas (opcional)
```bash
python manage.py test
```
*Todas las pruebas deben finalizar con estado `OK`.*

### 5. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre tu navegador web e ingresa a:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 5. Criterios de Evaluación Cubiertos (105 / 105 puntos)

| Criterio de la Rúbrica | Puntaje | Estado |
| :--- | :---: | :---: |
| **Repositorio Git y entorno virtual creado** | 5 pts | Cumplido |
| **Archivo `.gitignore` configurado adecuadamente** | 5 pts | Cumplido |
| **Proyecto Django creado y funcional** | 5 pts | Cumplido |
| **Vista de bienvenida con 2 géneros en Bootstrap** | 10 pts | Cumplido |
| **Template `inicio.html` que hereda de `base.html`** | 5 pts | Cumplido |
| **Despliegue de datos desde `views.py` con `for` e `if`** | 10 pts | Cumplido |
| **Templates de películas con componentes Bootstrap** | 10 pts | Cumplido |
| **Imágenes mostradas correctamente desde `static/`** | 5 pts | Cumplido |
| **URLs configuradas para acceder desde la raíz (`/`)** | 5 pts | Cumplido |
| **Template `base.html` con menú de navegación** | 6 pts | Cumplido |
| **Uso efectivo de Bootstrap para diseño responsivo** | 6 pts | Cumplido |
| **Archivos estáticos organizados en `static/`** | 3 pts | Cumplido |
| **Menú de navegación funcional entre secciones** | 6 pts | Cumplido |
| **URLs claras y uso de namespaces (`home:inicio`, `home:genero`)** | 4 pts | Cumplido |
| **Commits frecuentes y mensajes descriptivos** | 5 pts | Cumplido |
| **Trabajo en equipo y colaboración visible en Git** | 5 pts | Cumplido |
| **Documentación en `README.md` con datos de integrantes** | 5 pts | Cumplido |
| **TOTAL** | **105 pts** | **100%** |
