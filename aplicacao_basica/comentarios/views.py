from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Comentario
from notas.models import Nota
from .forms import ComentarioForm
from django.shortcuts import redirect

def lista_comentarios(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    comentarios = Comentario.objects.filter(nota=nota).order_by('-criado_em')

    # Se o método for POST, isso significa que o usuário está tentando adicionar um comentário
    if request.method == 'POST':
        form = ComentarioForm(request.POST)  # Cria um formulário com os dados recebidos
        if form.is_valid():  # Verifica se o formulário é válido
            comentario = form.save(commit=False)  # Cria uma instância do comentário, mas não salva ainda
            comentario.nota = nota  # Associa o comentário à nota correta
            comentario.save()  # Salva o comentário no banco de dados
            return redirect('lista_comentarios', nota_id=nota.id)  # Redireciona para a mesma página

    else:
        form = ComentarioForm()  # Se não for POST, cria um formulário vazio

    return render(request, 'comentarios/comentario_list.html', {
        'nota': nota,
        'comentarios': comentarios,
        'form': form,  # Passa o formulário para o template
    })


def adicionar_comentario(request, nota_id):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.nota_id = nota_id
            comentario.usuario = request.user if request.user.is_authenticated else None  # Deixa vazio se for anônimo
            comentario.save()
            return redirect('lista_comentarios', nota_id=nota_id)
    return redirect('lista_comentarios', nota_id=nota_id)
