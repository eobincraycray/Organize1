from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Tarefa, Categoria
from .forms import CategoriaForm

def home(request):
    return render( request, 'home.html')

@login_required
def lista_tarefas(request):
    # Buscar todas as tarefas do usuário logado
    tarefas = Tarefa.objects.filter(usuario=request.user, concluida=False)
    full_name = request.user.username  
    return render(request, 'lista_tarefa.html', {'tarefas': tarefas, 'full_name': full_name})

# Visualizar a tarefa
@login_required
def visualizar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    return render(request, 'visualizar_tarefa.html', {'tarefa': tarefa})

# Editar a tarefa
@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica para editar a tarefa, ex: atualizar título, descrição
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.save()
        return redirect('tarefa:lista_tarefas')  # Redireciona de volta para a lista de tarefas
    return render(request, 'editar_tarefa.html', {'tarefa': tarefa})

# Marcar a tarefa como concluída
@login_required
def marcar_concluida(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.concluida = True
    tarefa.save()
    return redirect('tarefa:lista_tarefas')

# Excluir a tarefa
@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.delete()
    return redirect('tarefa:lista_tarefas')

@login_required
def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        data_limite = request.POST.get('data_limite')

        categoria = Categoria.objects.get(id=categoria_id)  # Pega a categoria pelo ID

        # Cria a tarefa com os dados do formulário
        Tarefa.objects.create(
            usuario=request.user,
            titulo=titulo,
            descricao=descricao,
            categoria=categoria,
            data_limite=data_limite
        )

        return redirect('tarefa:lista_tarefas')

    # Se o método não for POST, renderiza o formulário
    categorias = Categoria.objects.all()  # Pega todas as categorias
    return render(request, 'adicionar_tarefa.html', {'categorias': categorias})

# Função para verificar se o usuário é admin
def is_admin(user):
    return user.is_staff  # Verifica se o usuário tem permissão de admin (é um staff no Django)

# Listar todas as categorias (admin)
@user_passes_test(is_admin)
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

# Criar uma nova categoria (admin)
# Criar uma nova categoria (admin)
@user_passes_test(is_admin)
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova categoria
            messages.success(request, 'Categoria criada com sucesso!')
            return redirect('tarefa:lista_categorias')
    else:
        form = CategoriaForm()  # Inicializa o formulário vazio
    return render(request, 'criar_categoria.html', {'form': form})

# Editar uma categoria existente (admin)
@user_passes_test(is_admin)
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()  # Salva as alterações na categoria
            messages.success(request, 'Categoria editada com sucesso!')
            return redirect('tarefa:lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)  # Preenche o formulário com os dados da categoria
    return render(request, 'editar_categoria.html', {'form': form, 'categoria': categoria})

# Visualizar uma categoria específica (admin)
@user_passes_test(is_admin)
def visualizar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'visualizar_categoria.html', {'categoria': categoria})

# Excluir uma categoria (admin)
@user_passes_test(is_admin)
def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)  # Obtém a categoria ou retorna 404
    categoria.delete()  # Exclui a categoria
    messages.success(request, "Categoria excluída com sucesso!")  # Mensagem de sucesso
    return redirect('tarefa:lista_categorias')  # Redireciona para a lista de categorias

@user_passes_test(is_admin)
def lista_todas_tarefas(request):
    tarefas = Tarefa.objects.all()  # Obtém todas as tarefas de todos os usuários
    return render(request, 'lista_todas_tarefas.html', {'tarefas': tarefas})