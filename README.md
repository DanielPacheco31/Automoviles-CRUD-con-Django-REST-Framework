# Documentación del Proyecto Django con REST Framework

## Estructura del Proyecto

Este proyecto Django implementa un sistema de gestión de automóviles con una API REST. La estructura general es la siguiente:

```
Daniel/                  # Proyecto Django principal
│
├── pacheciApp/         # Aplicación principal
│   ├── api/             # Paquete para la API REST
│   │   ├── __init__.py  # Inicialización del paquete
│   │   ├── router.py    # Definición de rutas de la API
│   │   ├── serializers.py # Serializadores para el modelo
│   │   └── views.py     # ViewSets para operaciones CRUD
│   │
│   ├── migrations/      # Migraciones de base de datos
│   ├── __init__.py      # Inicialización del paquete
│   ├── admin.py         # Configuración del panel de admin
│   ├── apps.py          # Configuración de la aplicación
│   ├── models.py        # Definición del modelo Automovil
│   ├── tests.py         # Pruebas unitarias
│   └── views.py         # Vistas de Django (sin usar en este proyecto)
│
├── nombre/              # Configuración del proyecto
│   ├── __init__.py      # Inicialización del paquete
│   ├── asgi.py          # Configuración ASGI
│   ├── settings.py      # Configuración del proyecto
│   ├── urls.py          # URLs del proyecto
│   └── wsgi.py          # Configuración WSGI
│
├── manage.py            # Script de administración de Django
└── db.sqlite3           # Base de datos SQLite (se crea al migrar)
```

## Modelo "Automovil"

El modelo `Automovil` está definido en `pachecoApp/models.py` con los siguientes campos:

- **nombre**: Campo de texto para el nombre del automóvil
- **marca**: Campo de texto para la marca del automóvil
- **modelo**: Campo numérico para el año o modelo del automóvil
- **diseño**: Campo de texto para el diseño o tipo de carrocería
- **cilindraje**: Campo numérico para el cilindraje del motor

## Panel de Administración

El modelo está registrado en el panel de administración de Django a través de `pachecoApp/admin.py`. La clase `AutomovilAdmin` personaliza la visualización con:

- Lista de campos visibles (list_display)
- Campos de búsqueda (search_fields)
- Filtros (list_filter)

Para acceder al panel de administración:
1. Crear un superusuario: `python manage.py createsuperuser`
2. Iniciar el servidor: `python manage.py runserver`
3. Acceder a: `http://localhost:8000/admin/`

## API REST

La API REST implementada con Django REST Framework permite operaciones completas de CRUD (Crear, Leer, Actualizar, Eliminar) sobre el modelo Automovil.

### Endpoints de la API

| Método | URL                               | Descripción                            |
|--------|-----------------------------------|----------------------------------------|
| GET    | `/api/automoviles/`               | Listar todos los automóviles           |
| POST   | `/api/automoviles/`               | Crear un nuevo automóvil               |
| GET    | `/api/automoviles/{id}/`          | Obtener un automóvil específico        |
| PUT    | `/api/automoviles/{id}/`          | Actualizar un automóvil completo       |
| PATCH  | `/api/automoviles/{id}/`          | Actualizar campos parciales            |
| DELETE | `/api/automoviles/{id}/`          | Eliminar un automóvil                  |

### Ejemplos de uso

#### Listar todos los automóviles
```
GET /api/automoviles/
```

Respuesta:
```json
[
    {
        "id": 1,
        "nombre": "atracttive",
        "marca": "fiat",
        "modelo": 2012,
        "diseño": "compacto",
        "cilindraje": 1
    },
    {
        "id": 2,
        "nombre": "Mustang",
        "marca": "Ford",
        "modelo": 1999,
        "diseño": "compacto",
        "cilindraje": 4
    }
]
```

#### Crear un nuevo automóvil
```
POST /api/automoviles/
```

Datos:
```json
{
    "nombre": "Civic",
    "marca": "Honda",
    "modelo": 2023,
    "diseño": "Sedan",
    "cilindraje": 2
}
```

#### Obtener un automóvil específico
```
GET /api/automoviles/1/
```

Respuesta:
```json
{
    "id": 1,
    "nombre": "Sentra",
    "marca": "Nissan",
    "modelo": 2022,
    "diseño": "Sedán",
    "cilindraje": 1
}
```


## Pruebas

Puedes probar la API utilizando herramientas como:
- El navegador web para peticiones GET
- Postman o Insomnia para probar todos los métodos HTTP
- curl desde la línea de comandos
