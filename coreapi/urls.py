from django.urls import path, include
from .views import overview, taskList, taskDetail, taskCreate, taskUpdate, taskDelete
from django.views.generic import TemplateView

app_name = 'coreapi'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('overview/', overview, name='overview'),
    path('task-list/', taskList, name='task-list'),
    path('task-detail/<int:pk>/', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-update/<int:pk>/', taskUpdate, name='task-update'),
    path('task-delete/<int:pk>/', taskDelete, name='task-update'),
]
