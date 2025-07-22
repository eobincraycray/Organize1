from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm  # Formulário para editar o perfil
from tarefa import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm

# Página de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser:
                return redirect('usuario:dashboard_admin')  # Redirecione para a interface do admin
            else:
                return redirect('tarefa:lista_tarefas')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Página de registro
def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('usuario:login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})

# Página de perfil (apenas usuários autenticados)
@login_required
def perfil(request):
    return render(request, 'perfil.html')

# Edição de perfil (apenas usuários autenticados)
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('usuario:perfil')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

@login_required
def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')


@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario:lista_usuarios')
    else:
        form = UserChangeForm(instance=usuario)

    return render(request, 'editar_perfil.html', {'form': form, 'usuario': usuario})


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def excluir_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    # Proteção para não excluir a si mesmo
    if request.user == usuario:
        messages.error(request, "Você não pode excluir a si mesmo.")
        return redirect('usuario:lista_usuarios')

    usuario.delete()
    messages.success(request, "Usuário excluído com sucesso.")
    return redirect('usuario:lista_usuarios')

@login_required
@user_passes_test(is_admin)
def criar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            messages.success(request, "Usuário criado com sucesso.")
            return redirect('usuario:lista_usuarios')
    else:
        form = UserCreationForm()

    return render(request, 'criar_usuario.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def visualizar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    return render(request, 'visualizar_usuario.html', {'usuario': usuario})