from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TasksForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# create your views here

def index(request):
    tasks = Tasks.objects.all()

    form = TasksForm()
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'tasks': tasks, 'form': form}

    return render(request, 'tasks/list.html', context)


def updatetask(request, pk):
    task = Tasks.objects.get(pk=pk)
    form = TasksForm(instance=task)
    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deletetask(request, pk):
    item = Tasks.objects.get(pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasks/delete.html', context)


# @login_required
# # views.py
# def task_list(request):
#     user_tasks = Tasks.objects.filter(user=request.user)
#     sorted_tasks = user_tasks.order_by('-due_date')
#
#
# class TaskListView(ListView):
#     model = Tasks
#     template_name = 'tasks/list.html'
#     context_object_name = 'tasks'
#
#
# class TaskDetailView(DetailView):
#     model = Tasks
#     template_name = 'tasks/detail.html'
#     context_object_name = 'task'
#
#
# class TaskCreateView(CreateView):
#     model = Tasks
#     form_class = TasksForm
#     template_name = 'tasks/create.html'
#     success_url = reverse_lazy('tasks:task_list')
#
#
# class TaskUpdateView(UpdateView):
#     model = Tasks
#     form_class = TasksForm
#     template_name = 'tasks/update.html'
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks:task_list')
#
#
# class TaskCompleteView(UpdateView):
#     model = Tasks
#     template_name = 'tasks/complete.html'
#     context_object_name = 'task'
#     fields = ['completed']
#     success_url = reverse_lazy('tasks:task_list')
#
#
# class TaskDeleteView(DeleteView):
#     model = Tasks
#     template_name = 'tasks/delete.html'
#     context_object_name = 'task'
#     success_url = reverse_lazy('tasks:task_list')
