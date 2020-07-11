from django.shortcuts import render, redirect
from.models import *
from django.contrib import messages 

def index(request):
    context ={
        'courses' : Course.objects.all()
    }
    return render(request, 'home.html',context)

def add_course(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['desc']
        )
        return redirect('/')

def verify(request, id):
    context ={
        'this_course' : Course.objects.get(id=id)
    }
    return render(request, 'delete.html', context)

def delete(request, id):
    if request.method == "POST":
        this_course = Course.objects.get(id=id)
        this_course.delete()
        return redirect('/')
