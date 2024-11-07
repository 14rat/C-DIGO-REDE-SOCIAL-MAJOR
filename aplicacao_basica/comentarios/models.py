from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from notas.models import Nota

class Comentario(models.Model):
    nota = models.ForeignKey(Nota, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User,null = True, blank=True, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.usuario.username}: {self.texto}'
