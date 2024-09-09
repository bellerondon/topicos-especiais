# tasks/admin.py

from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'assigned_to')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
