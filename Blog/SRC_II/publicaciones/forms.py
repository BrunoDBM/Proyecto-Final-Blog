from django import forms
from .models import Publicacion


class Publicarform(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'cuerpo', 'categoria', 'creador']

