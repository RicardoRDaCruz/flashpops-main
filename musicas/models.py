from django.db import models

# Create your models here.

JOGO_CHOICES = [
    ('1', 'um'),
    ('2', 'dois'),
    ('3', 'tres'),
    ('4', 'quatro'),
]

class Musica(models.Model):
    filme = models.CharField(max_length=100)
    posicao = models.IntegerField()
    file=models.FileField(upload_to='audio')
    jogo = models.CharField(
        max_length=2,
        choices=JOGO_CHOICES,
        default='um',
    )

class NomeAlternativo(models.Model):
    nome=models.CharField(max_length=100)
    musica=models.ForeignKey(Musica, on_delete=models.CASCADE)

