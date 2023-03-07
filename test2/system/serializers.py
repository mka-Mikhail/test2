from rest_framework import serializers

from system.models import Task


class TaskSerializerForCreateUpdate(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description']


class TaskSerializerForGet(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'date_updated', 'time_updated', 'date_created']
