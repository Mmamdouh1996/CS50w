from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    context = {
        "newyear": now.day == 1 and now.month == 1
    }
    return render(request, 'newyear/index.html', context)
