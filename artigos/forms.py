from django import forms
from .models import Artigo, Comentario


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ["titulo", "texto", "fotografia", "link_externo"]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["autor", "texto"]
        widgets = {
            "autor": forms.TextInput(attrs={
                "placeholder": "O teu nome",
                "aria-label": "Nome",
            }),
            "texto": forms.Textarea(attrs={
                "placeholder": "Escreve um comentário...",
                "rows": 2,
                "aria-label": "Comentário",
            }),
        }