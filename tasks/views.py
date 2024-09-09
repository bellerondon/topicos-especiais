# tasks/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.db.models import Q

@login_required
def task_list(request):
    status_filter = request.GET.get('status')
    if status_filter:
        tasks = Task.objects.filter(assigned_to=request.user, status=status_filter)
    else:
        tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'status_filter': status_filter})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Verifica se o usuário é responsável pela tarefa ou é staff
    if task.assigned_to != request.user and not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para visualizar esta tarefa.')
        return redirect('task_list')
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'Tarefa "{task.title}" criada com sucesso!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Criar Tarefa'})

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Verifica se o usuário é responsável pela tarefa ou é staff
    if task.assigned_to != request.user and not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para editar esta tarefa.')
        return redirect('task_list')
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tarefa "{task.title}" atualizada com sucesso!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Editar Tarefa'})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Verifica se o usuário é responsável pela tarefa ou é staff
    if task.assigned_to != request.user and not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para deletar esta tarefa.')
        return redirect('task_list')
    if request.method == 'POST':
        task.delete()
        messages.success(request, f'Tarefa "{task.title}" deletada com sucesso!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def dashboard(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão para acessar o dashboard.')
        return redirect('task_list')
    tasks = Task.objects.all()
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})
