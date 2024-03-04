API de Equipos de Fútbol
Esta es una API simple para administrar equipos de fútbol. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar información sobre equipos de fútbol, incluyendo su nombre, entrenador, capitán y liga.

Instalación
Clona este repositorio:
bash
Copy code
git clone <URL_DEL_REPOSITORIO>
Instala las dependencias:
Copy code
pip install fastapi uvicorn
Ejecuta la aplicación:
css
Copy code
uvicorn main:app --reload
La API estará disponible en http://localhost:8000.

Uso
Crear un nuevo equipo
css
Copy code
POST /equipos/

Body:
{
    "nombre": "Nombre del equipo",
    "entrenador": "Nombre del entrenador",
    "capitan": "Nombre del capitán",
    "liga": "Nombre de la liga"
}
Obtener todos los equipos
bash
Copy code
GET /equipos/
Obtener un equipo por su ID
bash
Copy code
GET /equipos/{equipo_id}
Actualizar un equipo por su ID
css
Copy code
PUT /equipos/{equipo_id}

Body:
{
    "nombre": "Nuevo nombre del equipo",
    "entrenador": "Nuevo nombre del entrenador",
    "capitan": "Nuevo nombre del capitán",
    "liga": "Nuevo nombre de la liga"
}
Eliminar un equipo por su ID
bash
Copy code
DELETE /equipos/{equipo_id}
Contribuir
Si quieres contribuir a este proyecto, por favor abre un issue o envía un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.