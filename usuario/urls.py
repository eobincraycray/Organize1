from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar, name='registrar'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('logout/', LogoutView.as_view(next_page='tarefa:home'), name='logout'),
    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('admin/usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('admin/usuarios/<int:user_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('admin/usuarios/excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('admin/usuarios/criar/', views.criar_usuario, name='criar_usuario'),
    path('admin/usuarios/<int:user_id>/', views.visualizar_usuario, name='visualizar_usuario'),
]