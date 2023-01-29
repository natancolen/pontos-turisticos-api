from django.db import models

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.TextField(max_length=250, blank=True, null=True)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
