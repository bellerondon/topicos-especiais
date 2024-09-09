from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Página de listagem de tarefas
    path('create/', views.task_create, name='task_create'),  # Página de criação de tarefas
    path('<int:task_id>/', views.task_detail, name='task_detail'),  # Página de detalhes da tarefa
    path('<int:task_id>/edit/', views.task_edit, name='task_edit'),  # Página de edição de tarefas
    path('<int:task_id>/delete/', views.task_delete, name='task_delete'),  # Página de exclusão de tarefas
]
