# forms.py
from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', 'prioridade']  # Inclui todos os campos
        widgets = {
            'prioridade': forms.Select(choices=Categoria._meta.get_field('prioridade').choices)  # Acesso correto ao choices
        }