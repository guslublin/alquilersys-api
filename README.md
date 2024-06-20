# alquilersys-api
Sistema de alquileres de libros - Backend


# Instalar dependencias necesarias
pip install django
pip install django-cors-headers
pip install psycopg2-binary

# Encender base de datos Postgres con docker
docker run --name alquilersys_postgres -e POSTGRES_DB=alquilersys -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:latest

# Ejecutar las migraciones de las tablas
python3 manage.py migrate

