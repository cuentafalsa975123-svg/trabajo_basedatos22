from django import forms

from .models import Interes

INPUT_STYLE = "width:100%;"


class InteresForm(forms.ModelForm):
    class Meta:
        model = Interes
        fields = ["nombre", "categoria", "nivel", "notas"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Ej: Fotografía analógica"}),
            "notas": forms.Textarea(attrs={"rows": 4, "placeholder": "¿Qué te gusta de esto? ¿Qué quieres lograr?"}),
        }
        labels = {
            "nombre": "¿Cuál es tu hobby o interés?",
            "categoria": "Categoría",
            "nivel": "Tu nivel actual",
            "notas": "Notas",
        }
