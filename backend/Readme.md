# Proyecto Django

Este es un proyecto Django configurado para ejecutarse en un entorno virtual (venv). A continuación se detallan los pasos para instalarlo, configurarlo y ejecutarlo.

## Requisitos previos

- Python 3.x (recomendado Python 3.8 o superior)
- PostgreSQL (si se está utilizando PostgreSQL como base de datos)
- Git (opcional, si quieres clonar el repositorio desde un sistema de control de versiones)

## Instalación

### 1. Clona el repositorio (opcional)

Si tienes un repositorio remoto, clónalo usando Git:

```bash
git clone https://github.com/usuario/proyecto-django.git
cd proyecto-django
```

### 2. Crea y activa un entorno virtual

En la carpeta raíz del proyecto, crea un entorno virtual llamado `venv`:

```bash
python -m venv venv
```

Luego, activa el entorno virtual:

- En Windows:

```bash
venv\Scripts\activate
```

- En macOS y Linux:

```bash
source venv/bin/activate
```

### 3. Instala las dependencias

Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

Copia el archivo `.env.example` y renómbralo a `.env`. Luego, configura las variables de entorno según tus necesidades.

```env
# .env
DEBUG=True
SECRET_KEY=tu_secret_key_segura
DATABASE_NAME=nombre_de_la_base_de_datos
DATABASE_USER=usuario
DATABASE_PASSWORD=contraseña
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
### 5. Realiza las migraciones
Django utiliza migraciones para configurar el esquema de la base de datos. Ejecuta las siguientes instrucciones para aplicar las migraciones necesarias:

```bash	
python manage.py migrate
```

### 6. Crear un superusuario (opcional)
Si deseas acceder al panel de administración de Django, crea un superusuario con el siguiente comando:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones en pantalla para definir un usuario y contraseña.

### 7. Ejecuta el servidor de desarrollo

Inicia el servidor de Django con el siguiente comando:

```bash
python manage.py runserver
```

El servidor estará disponible en http://127.0.0.1:8000/.

## Archivos importantes
`manage.py`: Herramienta de línea de comandos para interactuar con el proyecto Django.
`requirements.txt`: Archivo que contiene todas las dependencias del proyecto.
`settings.py`: Archivo de configuración de Django, donde puedes ajustar la base de datos, el idioma, la zona horaria, etc.