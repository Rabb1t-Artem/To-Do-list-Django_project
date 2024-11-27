# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from to_do_list.models import Tag, Task
from to_do_list.forms import TaskForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "to_do_list/index.html")


def status_change(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("to_do_list:task-list")


# ----------------------------Tasks----------------------------------------


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    paginate_by = 10


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:task-list")


# ----------------------Tags-----------------------------------------------


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("to_do_list:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("to_do_list:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tag-list")
