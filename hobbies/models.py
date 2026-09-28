from django.db import models


class Interes(models.Model):
    """Un hobby o interés que el usuario quiere trackear, al estilo de una nota."""

    CATEGORIA_CHOICES = [
        ("deporte", "Deporte"),
        ("arte", "Arte y manualidades"),
        ("musica", "Música"),
        ("tecnologia", "Tecnología"),
        ("lectura", "Lectura"),
        ("aire_libre", "Aire libre"),
        ("cocina", "Cocina y gastronomía"),
        ("juegos", "Juegos"),
        ("otro", "Otro"),
    ]

    NIVEL_CHOICES = [
        ("principiante", "Principiante"),
        ("intermedio", "Intermedio"),
        ("avanzado", "Avanzado"),
    ]

    nombre = models.CharField("Nombre del hobby/interés", max_length=100)
    categoria = models.CharField("Categoría", max_length=20, choices=CATEGORIA_CHOICES, default="otro")
    nivel = models.CharField("Nivel", max_length=20, choices=NIVEL_CHOICES, default="principiante")
    notas = models.TextField("Notas", blank=True, help_text="Como una nota libre: qué te gusta, qué quieres lograr, etc.")
    fecha_agregado = models.DateTimeField("Fecha en que se agregó", auto_now_add=True)

    class Meta:
        verbose_name = "Interés"
        verbose_name_plural = "Intereses"
        ordering = ["-fecha_agregado"]

    def __str__(self):
        return self.nombre

    def recursos_relacionados(self):
        """Recursos sugeridos que comparten la misma categoría que este interés."""
        return RecursoSugerido.objects.filter(categoria=self.categoria)


class RecursoSugerido(models.Model):
    """Un lugar/comunidad/sitio donde se puede explorar una categoría de interés."""

    TIPO_CHOICES = [
        ("tienda", "Tienda"),
        ("comunidad", "Comunidad o club"),
        ("evento", "Evento"),
        ("web", "Sitio web"),
        ("curso", "Curso o taller"),
    ]

    categoria = models.CharField("Categoría", max_length=20, choices=Interes.CATEGORIA_CHOICES)
    nombre_lugar = models.CharField("Nombre", max_length=150)
    tipo = models.CharField("Tipo de recurso", max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField("Descripción", blank=True)
    enlace = models.URLField("Enlace o referencia", blank=True)

    class Meta:
        verbose_name = "Recurso sugerido"
        verbose_name_plural = "Recursos sugeridos"
        ordering = ["categoria", "nombre_lugar"]

    def __str__(self):
        return f"{self.nombre_lugar} ({self.get_categoria_display()})"
