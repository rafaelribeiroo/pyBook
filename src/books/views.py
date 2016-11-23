from django.shortcuts import render

from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import LivroForm

# Create your views here.
from .models import Livro

def livro(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

def criarLivro(request):
    form = LivroForm()
    context = {'form': form}
    html_form = render_to_string('cadastraLivro.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})
