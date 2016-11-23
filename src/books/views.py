from django.shortcuts import render

# Create your views here.
from .models import Livro

def livro(request):
    livros = Livro.objects.all()
    return render(request, 'livro_list.html', {'livros': livros})
