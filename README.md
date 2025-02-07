# CrudPython
CrudPython es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) construida con FastAPI y MySQL. Este proyecto sirve como un ejemplo de cómo construir una API RESTful utilizando FastAPI y SQLAlchemy para la gestión de la base de datos.
## APIs Disponibles

### Usuarios

- **GET /users/**: Obtiene una lista de usuarios.
- **POST /user/{id}**: Obtiene un usuario por su ID.
- **POST /users/**: Crea un nuevo usuario.
- **PUT /users/{id}**: Actualiza un usuario existente por su ID.
- **DELETE /users/{id}**: Elimina un usuario por su ID.

### Materiales

- **GET /materials/**: Obtiene una lista de materiales.
- **GET /materials/{material_id}**: Obtiene un material por su ID.
- **POST /materials/**: Crea un nuevo material.
- **PUT /materials/{material_id}**: Actualiza un material existente por su ID.
- **DELETE /materials/{material_id}**: Elimina un material por su ID.

### Préstamos

- **GET /loans/**: Obtiene una lista de préstamos.
- **GET /loans/{prestamo_id}**: Obtiene un préstamo por su ID.
- **POST /loans/**: Crea un nuevo préstamo.
- **PUT /loans/{prestamo_id}**: Actualiza un préstamo existente por su ID.
- **DELETE /loans/{prestamo_id}**: Elimina un préstamo por su ID.




