from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task


# Create your views here.

@api_view(['GET'])
def overview(request):
    api_urls = {
        'Task-List': '/task-list/',
        'Task-Details': '/task-detail/<int:pk>/',
        'Create-Task': '/task-create/',
        'Update-Task': '/task-update/<int:pk>/',
        'Delete': '/task-delete/<int:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('Item was successfully deleted!')
