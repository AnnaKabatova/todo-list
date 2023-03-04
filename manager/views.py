from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "manager/task_lsit.html"
    paginate_by = 4


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
    form_class = TaskForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 4
    template_name = "manager/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "manager/tag_form.html"
    success_url = reverse_lazy("manager:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "manager/tag_form.html"
    success_url = reverse_lazy("manager:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "manager/tag_confirm_delete.html"
    success_url = reverse_lazy("manager:tag-list")
