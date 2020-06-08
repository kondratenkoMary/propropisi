# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from caching.base import CachingMixin, CachingManager
from imagefield.fields import ImageField


def thumb(fieldfile, context):
    context.processors = [
        "force_jpeg",
        ("crop", (70, 70)),
    ]


img_formats = {
    'thumb': thumb
}


class Task(CachingMixin, models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(default='')
    deadline = models.DateTimeField(default=timezone.now)

    objects = CachingManager()
    teacher = CachingManager()

    def __str__(self):
        return self.title


class ClassName(CachingMixin, models.Model):
    teacher = models.ForeignKey('Teacher', related_name='classes', on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    objects = CachingManager()

    def __str__(self):
        return self.name


class Student(User):
    classname = models.ForeignKey(ClassName, related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    img = ImageField(upload_to='students', formats=img_formats, auto_add_fields=True, blank=True, null=True)
    avg_mark = models.FloatField(default=5)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'


class Solution(CachingMixin, models.Model):
    class SolutionStatus:
        Todo = 0
        Checking = 1
        Done = 2
        Expired = 3

    SolutionStatusChoices = (
        (SolutionStatus.Todo, 'Не выполнено'),
        (SolutionStatus.Checking, 'На проверке'),
        (SolutionStatus.Done, 'Проверенно'),
        (SolutionStatus.Expired, 'Просрочено')
    )

    task = models.ForeignKey(Task, related_name='solutions', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='solutions', on_delete=models.CASCADE)
    date_check = models.DateTimeField(blank=True, null=True)
    date_loading = models.DateTimeField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    mark_ai = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(choices=SolutionStatusChoices, default=SolutionStatus.Todo)
    file_name = models.CharField(null=True, blank=True, max_length=256)
    percent = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to='solutions')

    objects = CachingManager()

    def __str__(self):
        return '%s: %s' % (self.student.name, self.task.title)

    # class Meta:
    #     unique_together = ['task', 'student']


class Teacher(User):
    name = models.CharField(max_length=256)
    img = ImageField(upload_to='students', formats=img_formats, auto_add_fields=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
