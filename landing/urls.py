from django.urls import path
from .views import index, registrar_clique, salvar_localizacao

urlpatterns = [
    path('', index, name='index'),
    path('registrar-clique/', registrar_clique, name='registrar_clique'),
    path('salvar-localizacao/', salvar_localizacao, name='salvar_localizacao'),
]