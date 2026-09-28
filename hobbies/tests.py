from django.test import TestCase
from django.urls import reverse

from .models import Interes, RecursoSugerido


def crear_interes(nombre="Ajedrez", categoria="juegos"):
    return Interes.objects.create(nombre=nombre, categoria=categoria, nivel="principiante")


class InteresModelTests(TestCase):
    def test_recursos_relacionados_filtra_por_categoria(self):
        """recursos_relacionados() solo devuelve recursos de la misma categoría."""
        interes = crear_interes(categoria="musica")
        recurso_match = RecursoSugerido.objects.create(
            categoria="musica", nombre_lugar="Academia X", tipo="curso"
        )
        RecursoSugerido.objects.create(
            categoria="deporte", nombre_lugar="Gimnasio Y", tipo="tienda"
        )
        self.assertQuerySetEqual(
            interes.recursos_relacionados(), [recurso_match]
        )


class IndexViewTests(TestCase):
    def test_sin_intereses_muestra_estado_vacio(self):
        """Si no hay intereses guardados, se muestra el mensaje de tablero vacío."""
        response = self.client.get(reverse("hobbies:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "corcho está vacío")

    def test_lista_intereses_existentes(self):
        interes = crear_interes(nombre="Fotografía")
        response = self.client.get(reverse("hobbies:index"))
        self.assertContains(response, "Fotografía")
        self.assertIn(interes, response.context["intereses"])


class DetailViewTests(TestCase):
    def test_muestra_nombre_y_recursos(self):
        interes = crear_interes(nombre="Pintura", categoria="arte")
        RecursoSugerido.objects.create(categoria="arte", nombre_lugar="Taller Z", tipo="curso")
        url = reverse("hobbies:detail", args=(interes.id,))
        response = self.client.get(url)
        self.assertContains(response, "Pintura")
        self.assertContains(response, "Taller Z")


class AgregarInteresViewTests(TestCase):
    def test_crear_interes_via_formulario(self):
        response = self.client.post(
            reverse("hobbies:agregar"),
            {"nombre": "Ciclismo", "categoria": "deporte", "nivel": "principiante", "notas": ""},
        )
        self.assertEqual(Interes.objects.filter(nombre="Ciclismo").count(), 1)
        self.assertEqual(response.status_code, 302)


class BuscarViewTests(TestCase):
    def test_busqueda_sin_resultados_ofrece_enlace_externo(self):
        response = self.client.get(reverse("hobbies:buscar"), {"q": "malabarismo"})
        self.assertContains(response, "No tenemos recursos guardados")

    def test_busqueda_con_resultados(self):
        RecursoSugerido.objects.create(categoria="tecnologia", nombre_lugar="Meetup Django", tipo="comunidad")
        response = self.client.get(reverse("hobbies:buscar"), {"q": "Django"})
        self.assertContains(response, "Meetup Django")
