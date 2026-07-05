from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='posts/')
    data = models.DateTimeField()

    def __str__(self):
        return self.titulo
