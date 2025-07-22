from django.urls import path
from . import views

app_name = 'tarefa'  

urlpatterns = [
    path('', views.home, name='home'), 
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefa/<int:id>/', views.visualizar_tarefa, name='visualizar_tarefa'),
    path('editar_tarefa/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('marcar_concluida/<int:id>/', views.marcar_concluida, name='marcar_concluida'),
    path('excluir_tarefa/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('visualizar/<int:id>/', views.visualizar_tarefa, name='visualizar_tarefa'),
    path('todas_tarefas/', views.lista_todas_tarefas, name='lista_todas_tarefas'),
    
     # URLs de Categorias
    path('categorias/', views.lista_categorias, name='lista_categorias'),  # Listar Categorias
    path('categorias/criar/', views.criar_categoria, name='criar_categoria'),  # Criar Categoria
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),  # Editar Categoria
    path('categorias/visualizar/<int:id>/', views.visualizar_categoria, name='visualizar_categoria'),  # Visualizar Categoria
    path('categorias/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),  # Excluir Categoria
]