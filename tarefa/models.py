from django.db import models
from django.contrib.auth.models import User  

class Categoria(models.Model):
    nome = models.CharField(max_length=100)  
    descricao = models.TextField(blank=True, null=True)  
    prioridade = models.CharField(
        max_length=10,
        choices=[  # Prioridade da categoria
            ('baixa', 'Baixa'),
            ('media', 'Média'),
            ('alta', 'Alta')
        ],
        default='media'  
    )

    def __str__(self):
        return self.nome 
    

class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True) 
    titulo = models.CharField(max_length=255) 
    descricao = models.TextField()  
    data_criacao = models.DateTimeField(auto_now_add=True)  
    data_limite = models.DateTimeField()  
    concluida = models.BooleanField(default=False) 

    def __str__(self):
        return self.titulo  