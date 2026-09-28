from django.urls import path

from . import views

app_name = "hobbies"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("agregar/", views.agregar_interes, name="agregar"),
    path("buscar/", views.buscar, name="buscar"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
