from django.urls import path
from . import views

urlpatterns = [
    path('<int:nota_id>/', views.lista_comentarios, name='lista_comentarios'),
    path('<int:nota_id>/adicionar/', views.adicionar_comentario, name='adicionar_comentario'),
]
