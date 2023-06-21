from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display=("title","description","completed")


#Register the Model

admin.site.register(Task,TaskAdmin)