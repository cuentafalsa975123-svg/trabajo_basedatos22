from django.contrib import admin

from .models import Interes, RecursoSugerido


@admin.register(Interes)
class InteresAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "nivel", "fecha_agregado"]
    list_filter = ["categoria", "nivel"]
    search_fields = ["nombre", "notas"]


@admin.register(RecursoSugerido)
class RecursoSugeridoAdmin(admin.ModelAdmin):
    list_display = ["nombre_lugar", "categoria", "tipo", "enlace"]
    list_filter = ["categoria", "tipo"]
    search_fields = ["nombre_lugar", "descripcion"]
