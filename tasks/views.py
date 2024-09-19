from django.shortcuts import render
from .models import Task
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class AddTaskForm(forms.Form):
    name = forms.CharField(max_length=60)
    description = forms.CharField(max_length=1000)
    start_date = forms.DateField()
    end_date = forms.DateField()
    
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "tasks/index.html", {
            "tasks": request.user.tasks.all()
        })

def add(request):
    if request.method == "POST":
        task = AddTaskForm(request.POST)
        if task.is_valid():
            name = task.cleaned_data["name"]
            description = task.cleaned_data["description"]
            start_date = task.cleaned_data["start_date"]
            end_date = task.cleaned_data["end_date"]
            Task.objects.create(name=name, description=description, start_date=start_date, end_date=end_date, created_by=request.user)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {
                "form": task
            })
    return render(request, "tasks/add.html", {
        "form": AddTaskForm()
    })

def task(request, task_id):
    return render(request, "tasks/task.html", {
        "task": Task.objects.get(pk=task_id)
    })
