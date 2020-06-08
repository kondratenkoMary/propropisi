from rest_framework import serializers
import copy
from django.utils import timezone

from tools.serializers import ImageField

from front import models
from .common import DATE_FORMAT


def round_percents(items):
    items_rounded_percents = copy.copy(items)
    sum = 0

    for item in items_rounded_percents:
        item = int(round(item))
        sum += item

    while sum != 100:
        rounded_sum_larger = sum > 100
        ind = 0
        max_diff = 0

        for i in range(len(items)):
            if (rounded_sum_larger and items_rounded_percents[i] > items[i]) or (
                not rounded_sum_larger and items_rounded_percents[i] < items[i]):
                diff = abs(items[i] - items_rounded_percents[i])
                if diff > max_diff:
                    max_diff = diff
                    ind = i

        modify_value = -1 if rounded_sum_larger else 1
        items_rounded_percents[ind] += modify_value
        sum += modify_value

    return items_rounded_percents


class StudentSerializer(serializers.ModelSerializer):
    classname = serializers.StringRelatedField()
    img = ImageField(
        formats=['thumb']
    )

    class Meta:
        model = models.Student
        fields = ['name', 'classname', 'img', 'avg_mark', 'solutions']


class SolutionSerializer(serializers.ModelSerializer):
    date_loading = serializers.DateTimeField(DATE_FORMAT)
    student = StudentSerializer()

    class Meta:
        model = models.Solution
        fields = ['id', 'date_loading', 'percent', 'status', 'img', 'file_name', 'student', 'mark', 'mark_ai']


class TaskSerializer(serializers.ModelSerializer):
    deadline = serializers.DateTimeField(DATE_FORMAT)
    percents = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    solutions = SolutionSerializer(many=True)

    def get_percents(self, obj):
        count = obj.solutions.count()
        done = obj.solutions.filter(status=models.Solution.SolutionStatus.Done).count() * 100
        check = obj.solutions.filter(status=models.Solution.SolutionStatus.Checking).count() * 100
        not_sent = obj.solutions.filter(
            status__in=[models.Solution.SolutionStatus.Todo, models.Solution.SolutionStatus.Expired]).count() * 100
        percents_list = [float(not_sent) / count, float(check) / count, float(done) / count]
        rounded_percents = round_percents(percents_list)

        percents = {
            'done': rounded_percents[0],
            'check': rounded_percents[1],
            'notSent': rounded_percents[2]
        }

        return percents

    def get_status(self, obj):
        return timezone.now() <= obj.deadline


    class Meta:
        model = models.Task
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    img = ImageField(
        formats=['thumb']
    )

    def get_tasks(self, obj):
        tasks = models.Task.teacher.filter(
            solutions__student__classname__in=obj.classes.all().values_list('id', flat=True))
        return TaskSerializer(tasks, many=True).data

    class Meta:
        model = models.Teacher
        fields = ['name', 'img', 'tasks']
