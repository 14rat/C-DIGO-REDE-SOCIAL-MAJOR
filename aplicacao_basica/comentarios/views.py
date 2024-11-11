from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .models import Like
from notas.models import Nota
from .forms import ComentarioForm
from django.shortcuts import redirect
import json

def lista_comentarios(request, nota_id):
    nota = get_object_or_404(Nota, id=nota_id)
    comentarios = Comentario.objects.filter(nota=nota).order_by('-criado_em')

 
    if request.method == 'POST':
        form = ComentarioForm(request.POST) 
        if form.is_valid(): 
            comentario = form.save(commit=False) 
            comentario.nota = nota
            comentario.save() 
            return redirect('lista_comentarios', nota_id=nota.id) 

    else:
        form = ComentarioForm()  

    return render(request, 'comentarios/comentario_list.html', {
        'nota': nota,
        'comentarios': comentarios,
        'form': form,  
    })


def adicionar_comentario(request, nota_id):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.nota_id = nota_id

            
            if request.user.is_authenticated:
                comentario.usuario = request.user
            else:
                comentario.usuario = None  

            comentario.save()
            return redirect('lista_comentarios', nota_id=nota_id)

    return redirect('lista_comentarios', nota_id=nota_id)


def curtir_comentario_ajax(request, comentario_id):
    if request.method == 'POST':
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)

        comentario = get_object_or_404(Comentario, id=comentario_id)

      
        usuario = request.user if request.user.is_authenticated else None

        
        like = Like.objects.filter(comentario=comentario, usuario=usuario).first()

        if like:
            like.delete()
            liked = False
        else:
            Like.objects.create(comentario=comentario, usuario=usuario)
            liked = True
        return JsonResponse({
            'likes_count': comentario.likes.count(),
            'liked': liked
        })

    return JsonResponse({'error': 'Método não permitido.'}, status=405)