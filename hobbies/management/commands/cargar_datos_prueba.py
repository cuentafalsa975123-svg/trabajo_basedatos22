from django.core.management.base import BaseCommand

from hobbies.models import Interes, RecursoSugerido


class Command(BaseCommand):
    help = "Carga datos de prueba (generados con apoyo de IA) para intereses y recursos sugeridos."

    def handle(self, *args, **options):
        intereses = [
            {"nombre": "Escalada en roca", "categoria": "deporte", "nivel": "principiante",
             "notas": "Quiero aprender técnica de pies antes de subir a rutas más difíciles."},
            {"nombre": "Acuarela", "categoria": "arte", "nivel": "intermedio",
             "notas": "Practicar degradados de agua y probar papel de grano grueso."},
            {"nombre": "Guitarra", "categoria": "musica", "nivel": "principiante",
             "notas": "Aprender acordes abiertos y una canción completa este mes."},
            {"nombre": "Programación en Python", "categoria": "tecnologia", "nivel": "avanzado",
             "notas": "Explorar Django más a fondo y APIs REST."},
            {"nombre": "Ciencia ficción", "categoria": "lectura", "nivel": "intermedio",
             "notas": "Terminar la saga de Fundación de Asimov."},
            {"nombre": "Senderismo", "categoria": "aire_libre", "nivel": "principiante",
             "notas": "Buscar rutas cortas cerca de Santiago para partir."},
        ]

        for data in intereses:
            Interes.objects.get_or_create(nombre=data["nombre"], defaults=data)

        recursos = [
            {"categoria": "deporte", "nombre_lugar": "Boulder Search Providencia", "tipo": "tienda",
             "descripcion": "Centro de escalada indoor con clases para principiantes.",
             "enlace": "https://www.google.com/search?q=boulder+search+providencia"},
            {"categoria": "deporte", "nombre_lugar": "Club de Andinismo local", "tipo": "comunidad",
             "descripcion": "Grupo que organiza salidas de escalada los fines de semana.", "enlace": ""},
            {"categoria": "arte", "nombre_lugar": "Taller de acuarela Barrio Italia", "tipo": "curso",
             "descripcion": "Clases grupales mensuales para todo nivel.", "enlace": ""},
            {"categoria": "musica", "nombre_lugar": "Academia de guitarra popular", "tipo": "curso",
             "descripcion": "Clases individuales y grupales de guitarra acústica.", "enlace": ""},
            {"categoria": "musica", "nombre_lugar": "Foro de guitarristas en español", "tipo": "web",
             "descripcion": "Comunidad online con tablaturas y consejos.",
             "enlace": "https://www.google.com/search?q=foro+guitarristas+en+espa%C3%B1ol"},
            {"categoria": "tecnologia", "nombre_lugar": "Documentación oficial de Django", "tipo": "web",
             "descripcion": "Guía oficial, tutoriales y referencia de la API.",
             "enlace": "https://docs.djangoproject.com/es/"},
            {"categoria": "tecnologia", "nombre_lugar": "Meetup de Python Chile", "tipo": "comunidad",
             "descripcion": "Encuentros mensuales de la comunidad Python en Chile.", "enlace": ""},
            {"categoria": "lectura", "nombre_lugar": "Librería Qué Leo", "tipo": "tienda",
             "descripcion": "Especializada en ciencia ficción y fantasía.", "enlace": ""},
            {"categoria": "lectura", "nombre_lugar": "Club de lectura de ciencia ficción", "tipo": "comunidad",
             "descripcion": "Se reúnen una vez al mes a discutir un libro.", "enlace": ""},
            {"categoria": "aire_libre", "nombre_lugar": "Sendero Cerro Manquehue", "tipo": "evento",
             "descripcion": "Ruta de dificultad media, ideal para empezar.", "enlace": ""},
            {"categoria": "aire_libre", "nombre_lugar": "Club de trekking Santiago", "tipo": "comunidad",
             "descripcion": "Organiza salidas grupales guiadas cada fin de semana.", "enlace": ""},
        ]

        for data in recursos:
            RecursoSugerido.objects.get_or_create(nombre_lugar=data["nombre_lugar"], defaults=data)

        self.stdout.write(self.style.SUCCESS(
            f"Listo: {Interes.objects.count()} intereses y {RecursoSugerido.objects.count()} recursos en la base de datos."
        ))
