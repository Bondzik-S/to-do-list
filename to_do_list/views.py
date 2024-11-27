
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm, TagForm
from .models import Task, Tag


def task_list(request):
    tasks = Task.objects.prefetch_related('tags').all()

    return render(request, "to_do_list/task_list.html", {"tasks": tasks})


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("to_do_list:task_list")
class TaskListView(generic.ListView):
    model = Task
    template_name = "to_do_list/task_list.html"
    context_object_name = "tasks"


class TagListView(generic.ListView):
    model = Tag
    template_name = "to_do_list/tag_list.html"
    context_object_name = "tags"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("to_do_list:task_list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("to_do_list:tag_list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "to_do_list/task_form.html"
    success_url = reverse_lazy("to_do_list:task_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "to_do_list/tag_form.html"
    success_url = reverse_lazy("to_do_list:tag_list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'to_do_list/task_confirm_delete.html'
    success_url = reverse_lazy("to_do_list:task_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'to_do_list/tag_confirm_delete.html'
    success_url = reverse_lazy("to_do_list:tag_list")