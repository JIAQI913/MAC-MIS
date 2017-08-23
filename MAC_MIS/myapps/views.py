import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django_tables2 import RequestConfig

from myapps.forms import LoginForm, ResetPasswordForm, StudentForm, FacultyForm, StaffForm
from myapps.models import MyUser, Student, Staff, Faculty, Project, Job
from myapps.tables import ProjectTable, JobTable


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapps:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.')
    else:
        form = LoginForm()
        return render(request, 'myapps/login.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapps:index'))





def index(request):
    return render(request, 'myapps/index.html')

@login_required
def update(request):
    user = get_object_or_404(MyUser, pk=request.user.id)
    if request.method=='POST':
        if user.is_Student:
            user = get_object_or_404(Student, pk=user.id)
            studentform = StudentForm(request.POST, instance=user)
            if studentform.is_valid():
                student = studentform.save()
        elif user.is_Faculty:
            user = get_object_or_404(Faculty, pk=user.id)
            facultyform = FacultyForm(request.POST, instance=user)
            if facultyform.is_valid():
                faculty = facultyform.save()
        elif user.is_staff:
            user = get_object_or_404(Staff, pk=user.id)
            staffform = StaffForm(request.POST, instance=user)
            if staffform.is_valid():
                faculty = staffform.save()
        return HttpResponseRedirect(reverse('myapps:index'))
    else:
        if user.is_Student:
            user = get_object_or_404(Student, pk=user.id)
            form = StudentForm(instance=user)
        elif user.is_Faculty:
            user = get_object_or_404(Faculty, pk=user.id)
            form = FacultyForm(instance=user)
        elif user.is_staff:
            user = get_object_or_404(Staff, pk=user.id)
            form = StaffForm(instance=user)
        return render(request,'myapps/update.html',{ 'form':form})

def forgetpassword(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = get_object_or_404(User, username = username)
        choice = "qwertyuiopasdfghjklzxcvbnm1234567890_"
        list = random.sample(choice, 9)
        #print(list)
        newpassword=""
        for i in list:
            newpassword += i
        print(newpassword)
        user.set_password(newpassword)
        user.save()
        temp = "Your password has been changed and your new password is " + newpassword +"."
        send_mail("Reset password", temp, "pythontest6666@gmail.com", [user.email], fail_silently=False)
        return HttpResponseRedirect(reverse('myapps:index'))
    else:
        form = ResetPasswordForm()
        return render(request, 'myapps/resetpassword.html', {'form':form})

@login_required
def resetpassword(request):
    if request.method == 'POST':
        password = request.POST['old_password']
        user = get_object_or_404(MyUser, pk=request.user.id)
        au_user = authenticate(username=user.username, password=password)
        if au_user:
            newpassword = request.POST['password']
            user.set_password(newpassword)
            user.save()
            return HttpResponseRedirect(reverse('myapps:login'))
    form = ResetPasswordForm()
    return render(request, 'myapps/resetpassword.html', {'form':form})

@login_required
def project(request):
    if request.method == 'POST':
        pass
    else:
        user=get_object_or_404(MyUser, pk=request.user.id)
        if user.is_Student:
            user = get_object_or_404(Student, pk=user.id)
            table = ProjectTable(Project.objects.filter(Stu_ID=user))
        elif user.is_Faculty:
            user = get_object_or_404(Faculty, pk=user.id)
            table = ProjectTable(Project.objects.filter(Fac_ID=user))
        elif user.is_staff:
            table = ProjectTable(Project.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'myapps/project.html', {'table': table})

@login_required
def job(request):
    if request.method == 'POST':
        pass
    else:
        user=get_object_or_404(MyUser, pk=request.user.id)
        if user.is_Student:
            user = get_object_or_404(Student, pk=user.id)
            table = JobTable(Job.objects.filter(Stu_ID=user))
        elif user.is_Faculty:
            user = get_object_or_404(Faculty, pk=user.id)
            table = JobTable(Job.objects.all())
        elif user.is_staff:
            table = JobTable(Job.objects.all())
        RequestConfig(request).configure(table)
        return render(request, 'myapps/job.html', {'table': table})