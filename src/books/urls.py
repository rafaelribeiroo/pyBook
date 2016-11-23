from django.conf.urls import url
from django.contrib import admin

from .views import (
    livro,
    criarLivro
    )

urlpatterns = [
    url(r'^$', livro, name='livro_lista'),
    url(r'^criar/$', criarLivro, name="livro_criar"),
]
