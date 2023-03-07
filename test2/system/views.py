from django.shortcuts import render
from rest_framework import generics
from system.models import Task
from system.serializers import TaskSerializerForCreateUpdate, TaskSerializerForGet


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForGet


class TaskRetrieve(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForGet


class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForCreateUpdate


class TaskDestroy(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForCreateUpdate


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerForCreateUpdate
