from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='index'),  # Página principal com a lista de notas
    path('criar/', views.criar_nota, name='criar_nota'),
    path('criar/form/', views.criar_form, name='criar_form'),
    path('criar/ajax/', views.criar_nota_ajax, name='criar_nota_ajax'),
    path('editar/<int:id>/', views.editar_nota, name='editar_nota'),
    path('excluir/<int:id>/', views.excluir_nota, name='excluir_nota'),  # URL para exclusão de nota
]
