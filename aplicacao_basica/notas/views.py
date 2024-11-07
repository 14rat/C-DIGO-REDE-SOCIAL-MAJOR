from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Nota
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/index.html', {'notas': notas})

def criar_nota(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        nota = Nota(titulo=titulo, conteudo=conteudo)
        nota.save()
        return JsonResponse({'status': 'success', 'titulo': titulo, 'conteudo': conteudo})
    return render(request, 'notas/criar_nota_form.html')

def criar_form(request):
    return render(request, 'notas/criar_nota_form.html')

@csrf_exempt
@require_POST
def criar_nota_ajax(request):
    titulo = request.POST.get('titulo')
    conteudo = request.POST.get('conteudo')
    nota = Nota(titulo=titulo, conteudo=conteudo)
    nota.save()
    return JsonResponse({
        'status': 'success',
        'id': nota.id,
        'titulo': titulo,
        'conteudo': conteudo
    })

def editar_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        nota.titulo = request.POST.get('titulo')
        nota.conteudo = request.POST.get('conteudo')
        nota.save()
        return redirect('index')
    return render(request, 'notas/editar_nota_form.html', {'nota': nota})

def excluir_nota(request, id):
    nota = get_object_or_404(Nota, id=id)
    if request.method == 'POST':
        nota.delete()
        return redirect('index')
    return render(request, 'notas/confirmar_exclusao.html', {'nota': nota})
