from django.contrib import admin
from django.contrib.admin import ModelAdmin


# Register your models here.
from myapps.models import Staff, Faculty, Student, Project, Job

admin.site.register(Staff)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Job)
