# recipe-app-api
Recipe API project

Comando para manipular

# los contenedores sigan corriendo en el fondo
docker compose up -d   

# Bajar Contenedores
docker compose down  

# Crear nueva carpeta App
docker compose run --rm app sh -c "python manage.py startapp {Nombre app}"


# Aplicar migraciones iniciales
docker compose run --rm app sh -c "python manage.py makemigrations"
docker compose run --rm app sh -c "python manage.py python manage.py migrate"
