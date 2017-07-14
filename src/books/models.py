from django.db import models
from django.utils.translation import ugettext_lazy as _


from .data import tiposLivro
# Create your models here.
class Livro(models.Model):
    titulo         = models.CharField('Título', max_length=50)
    dataPublicacao = models.DateField('Data de Publicação', null=True)
    autor          = models.CharField('Autor', max_length=30, blank=True)
    preco          = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    paginas        = models.IntegerField('Qntd. de Páginas', blank=True, null=True)
    tipoLivro      = models.PositiveSmallIntegerField('Tipo de Livro', choices=tiposLivro)

    class Meta:
        ordering = ['titulo']
        verbose_name = "livro"
        verbose_name_plural = "livros"

    def __str__(self):
        return self.titulo + ' - ' + self.autor
