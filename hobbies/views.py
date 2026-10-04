from urllib.parse import quote_plus

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

from .forms import InteresForm
from .models import Interes, RecursoSugerido
from rest_framework import viewsets, permissions
from .models import Interes
from .serializers import InteresSerializer

class InteresViewSet(viewsets.ModelViewSet):
    queryset = Interes.objects.all()
    serializer_class = InteresSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndexView(generic.ListView):
    """Lista todos los intereses guardados, como un tablero de notas."""

    template_name = "hobbies/index.html"
    context_object_name = "intereses"

    def get_queryset(self):
        return Interes.objects.all()


class DetailView(generic.DetailView):
    """Detalle de un interés: su nota y los recursos sugeridos según su categoría."""

    model = Interes
    template_name = "hobbies/detail.html"
    context_object_name = "interes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recursos"] = self.object.recursos_relacionados()
        return context


def agregar_interes(request):
    """Vista para crear una nueva nota de hobby/interés (operación de creación simple)."""
    if request.method == "POST":
        form = InteresForm(request.POST)
        if form.is_valid():
            interes = form.save()
            messages.success(request, f"Se agregó '{interes.nombre}' a tus intereses.")
            return redirect(reverse("hobbies:detail", args=(interes.id,)))
    else:
        form = InteresForm()
    return render(request, "hobbies/agregar.html", {"form": form})


def buscar(request):
    """
    Buscador: el usuario escribe un hobby/interés y la app le sugiere dónde
    puede encontrarlo (recursos cargados en la base de datos). Si no hay
    coincidencias exactas, se ofrece un enlace de búsqueda externo como
    alternativa.
    """
    query = request.GET.get("q", "").strip()
    resultados = []
    enlace_externo = None

    if query:
        resultados = RecursoSugerido.objects.filter(
            nombre_lugar__icontains=query
        ) | RecursoSugerido.objects.filter(
            categoria__icontains=query
        ) | RecursoSugerido.objects.filter(
            descripcion__icontains=query
        )
        resultados = resultados.distinct()

        if not resultados:
            enlace_externo = f"https://www.google.com/search?q={quote_plus(query + ' dónde practicar en Chile')}"

    return render(
        request,
        "hobbies/buscar.html",
        {
            "query": query,
            "resultados": resultados,
            "enlace_externo": enlace_externo,
        },
    )
