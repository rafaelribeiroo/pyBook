from django.db import models

# Create your models here.
class Livro(models.Model):
    Capadura = 1
    Simples = 2
    Digital = 3
    tiposLivro = (
        (Capadura, 'Capa Dura'),
        (Simples, 'Simples'),
        (Digital, 'E-book'),
    )
    titulo         = models.CharField('Título', max_length=50)
    dataPublicacao = models.DateField('Data de Publicação', null=True)
    autor          = models.CharField('Autor', max_length=30, blank=True)
    preco          = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    paginas        = models.IntegerField('Qntd. de Páginas', blank=True, null=True)
    tipoLivro      = models.PositiveSmallIntegerField('Tipo de Livro', choices=tiposLivro)
