from django.urls import path
from .views import task_list, task_status

urlpatterns = [
    path('tasks/', task_list),
    path('tasks/<int:pk>/status/', task_status),
]