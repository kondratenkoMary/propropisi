from rest_framework import serializers

from tools.serializers import ImageField

from front import models
from .common import DATE_FORMAT

class TaskSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(DATE_FORMAT)

    class Meta:
        model = models.Task
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    date_check = serializers.DateTimeField(DATE_FORMAT)
    date_loading = serializers.DateTimeField(DATE_FORMAT)

    class Meta:
        model = models.Solution
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    classname = serializers.StringRelatedField()
    img = ImageField(
        formats=['thumb']
    )
    solutions = SolutionSerializer(many=True)

    class Meta:
        model = models.Student
        fields = ['name', 'classname', 'img', 'avg_mark', 'solutions']
