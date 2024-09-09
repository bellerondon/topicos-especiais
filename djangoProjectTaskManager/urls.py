# djangoProjectTaskManager/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # URLs do app de usuários
    path('tasks/', include('tasks.urls')),  # URLs do app de tarefas
    # URLs de autenticação
    path('', lambda request: redirect('task_list')),  # Redirecionar a raiz (/) para a lista de tarefas
    path('accounts/', include('django.contrib.auth.urls')),  # Login e logout padrão do Django
]
