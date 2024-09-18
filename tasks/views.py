from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "tasks/index.html", {
            "tasks": request.user.tasks.all()
        })

# def add(request):

# def task(request, task_id):

