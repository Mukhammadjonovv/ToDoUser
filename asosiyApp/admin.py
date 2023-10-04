from django.contrib import admin
from .models import *

@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'status', 'detail']