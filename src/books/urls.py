from django.conf.urls import url
from django.contrib import admin

from .views import (
    livro,
    criarLivro,
    alteraLivro,
    deletaLivro
    )

urlpatterns = [
    url(r'^$', livro, name='livro_lista'),
    url(r'^criar/$', criarLivro, name="livro_criar"),
    url(r'^(?P<pk>\d+)/alterar/$', alteraLivro, name='livro_alterar'),
    url(r'^(?P<pk>\d+)/deletar/$', deletaLivro, name='livro_deletar'),
]
