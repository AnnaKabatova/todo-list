from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ("task_tag", "deadline", "created")


admin.site.register(Tag)
