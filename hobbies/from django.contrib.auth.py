from django.contrib.auth.models import User

# Listar todos los nombres de usuario y si son superusuarios
for user in User.objects.all():
    print(f"Usuario: {user.username} | Superusuario: {user.is_superuser}")