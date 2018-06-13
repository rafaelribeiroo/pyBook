from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model  = Livro
        fields =  ('titulo', 'dataPublicacao', 'autor', 'preco', 'paginas', 'tipoLivro', )
