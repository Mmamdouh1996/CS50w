from django.shortcuts import render

import tasks

tasks = ["foo", "bar", "baz"]

def index(request):
    context = {
        "tasks": tasks,
    }
    return render(request, 'tasks/index.html', context)

def add(request):
    return render(request, "tasks/add.html")