from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path('', views.index, name="index"),
    # path('add', views.add , name="add"),
    # path('task/<int:task_id>', views.task, name="task")
]