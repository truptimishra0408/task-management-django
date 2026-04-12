from django.urls import path
from . import views

urlpatterns = [
    path('mark-overdue/', views.mark_overdue),
    path('tasks/<int:task_id>/status/', views.update_task_status),
]