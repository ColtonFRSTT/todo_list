from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    print(tasks)
    context = {
        'tasks': tasks,
    }

    return render(request, 'task/index.html', context)