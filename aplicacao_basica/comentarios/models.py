from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from notas.models import Nota

class Comentario(models.Model):
    nota = models.ForeignKey(Nota, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null= True, blank = True, on_delete=models.CASCADE)  
    texto = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.usuario.username}: {self.texto}'

class Like(models.Model):
    comentario = models.ForeignKey(Comentario, related_name='likes', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  
    criado_em = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('comentario', 'usuario')

    def __str__(self):
        return f'{self.usuario.username} curtiu o comentário {self.comentario.id}'

