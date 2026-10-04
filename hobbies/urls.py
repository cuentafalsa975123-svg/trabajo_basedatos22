from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "hobbies"

router = DefaultRouter()
router.register(r'intereses', views.InteresViewSet)

urlpatterns = [
    # Endpoints de la API REST
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # Vistas HTML tradicionales
    path("", views.IndexView.as_view(), name="index"),
    path("agregar/", views.agregar_interes, name="agregar"),
    path("buscar/", views.buscar, name="buscar"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]