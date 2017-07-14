from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Livro
from .forms import LivroForm

def livro(request):
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

def salvar_form_livro(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            livros = Livro.objects.all()
            data['html_book_list'] = render_to_string('listaLivros.html', {
                'livros': livros
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def criarLivro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
    else:
        form = LivroForm()
    return salvar_form_livro(request, form, 'cadastraLivro.html')

def alteraLivro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
    else:
        form = LivroForm(instance=livro)
    return salvar_form_livro(request, form, 'alteraLivro.html')

def deletaLivro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    data = dict()
    if request.method == 'POST':
        livro.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        livros = Livro.objects.all()
        data['html_book_list'] = render_to_string('listaLivros.html', {
            'livros': livros
        })
    else:
        context = {'livro': livro}
        data['html_form'] = render_to_string('deletaLivro.html',
            context,
            request=request,
        )
    return JsonResponse(data)
