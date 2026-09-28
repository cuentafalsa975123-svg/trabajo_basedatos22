# Mi Cuaderno de Intereses (Hobby Tracker)

Aplicación web desarrollada con **Django** para llevar un registro tipo "nota" de tus hobbies e intereses, y descubrir dónde explorarlos.

## Descripción

Proyecto de evaluación del módulo *Desarrollo de aplicaciones del lado del servidor con Django e Inteligencia Artificial* (Evaluación 1).

La aplicación funciona como un cuaderno de notas: cada hobby o interés que agregas queda guardado como una "nota" (con categoría, nivel y apuntes libres), y la app te sugiere lugares, comunidades o sitios web relacionados con esa categoría. También incluye un buscador libre: si escribes cualquier interés, la app busca coincidencias en los recursos guardados y, si no encuentra nada, te ofrece un enlace de búsqueda externo como alternativa.

## Tecnologías utilizadas

- Python 3
- Django Framework
- SQLite (base de datos de desarrollo)
- HTML5, CSS3 (identidad visual propia tipo "corcho + notas adhesivas")
- Google Fonts (Kalam, Work Sans)
- django-widget-tweaks (paquete externo para controlar clases/atributos de campos de formulario desde el template)
- Inteligencia Artificial como apoyo al desarrollo

## Uso de Inteligencia Artificial en el desarrollo

**Apoyo al diseño de interfaces:** se usó IA para definir la identidad visual del sitio (paleta de colores, tipografías y el concepto de "corcho con notas adhesivas" para representar los intereses guardados, en vez de un listado genérico), y para revisar la consistencia del CSS entre las distintas plantillas. Cada sugerencia se validó levantando el servidor local y revisando el resultado en el navegador.

**Generación de datos de prueba:** los 6 intereses de ejemplo (escalada, acuarela, guitarra, programación, lectura, senderismo) y los 11 recursos sugeridos asociados se generaron con apoyo de IA y se cargan mediante un comando de gestión propio:

```
python manage.py cargar_datos_prueba
```

Los datos se revisaron manualmente para verificar que las categorías coincidieran correctamente entre `Interes` y `RecursoSugerido`, y que la información fuera realista para el contexto chileno.

## Protocolos, servicios de hosting y dominios

En desarrollo la app corre sobre **HTTP** local (`python manage.py runserver`, por defecto en `http://127.0.0.1:8000/`). El archivo `mysite/wsgi.py` es el punto de entrada estándar para que un servidor de aplicaciones (Gunicorn, uWSGI) comunique las peticiones HTTP con la lógica de Django en un entorno de producción.

Para desplegar esta aplicación fuera del entorno local se necesitaría:

- Un **hosting** compatible con Python/Django (por ejemplo PythonAnywhere, Render o Railway), configurando `DEBUG = False`, una base de datos de producción (PostgreSQL en vez de SQLite) y sirviendo los archivos estáticos con `collectstatic`.
- Un **dominio** propio (ej. `micuadernodeintereses.cl`) agregado a `ALLOWED_HOSTS`, con sus registros DNS (A/CNAME) apuntando al servidor donde quede alojada la aplicación.
- **HTTPS** en producción, delegando la terminación TLS al proveedor de hosting o a un servidor web como Nginx, en vez del HTTP plano que se usa en desarrollo.

## Estructura del proyecto (MVC)

| Componente | Descripción |
|------------|-------------|
| **Models** | `Interes` (hobby/nota del usuario) y `RecursoSugerido` (lugares/comunidades por categoría) |
| **Views**  | `IndexView` y `DetailView` (basadas en clases), `agregar_interes` y `buscar` (basadas en funciones) |
| **Templates** | Sistema reutilizable con `base.html` y herencia de templates (`index`, `detail`, `agregar`, `buscar`) |

## Funcionalidades principales

- **Tablero de notas:** lista todos los intereses guardados como notas adhesivas sobre un corcho.
- **Agregar interés:** formulario para crear una nueva nota (nombre, categoría, nivel, notas libres).
- **Detalle de la nota:** muestra los apuntes del interés y los recursos sugeridos de su misma categoría.
- **Buscador:** permite buscar por palabra clave entre los recursos guardados; si no hay coincidencias, ofrece un enlace de búsqueda externo.
- **Panel de administración de Django:** gestión de `Interes` y `RecursoSugerido` con filtros y búsqueda.

## Cómo ejecutar el proyecto

```
# 1. Entrar a la carpeta del proyecto
cd djangotutorial

# 2. Instalar dependencias
pip install django django-widget-tweaks

# 3. Crear la base de datos
python manage.py migrate

# 4. Cargar datos de prueba (opcional pero recomendado)
python manage.py cargar_datos_prueba

# 5. (Opcional) Crear usuario admin
python manage.py createsuperuser

# 6. Iniciar el servidor
python manage.py runserver
```

Luego visita `http://127.0.0.1:8000/` para ver el tablero de intereses.
