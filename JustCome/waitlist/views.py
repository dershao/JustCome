from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

queue = []

# Create your views here.
def queue(request):
    return render(request, 'waitlist/page.html')

def data(request):
    increment = request.GET.get("delta")
    if (increment == 1):
        queue.append(1)
    else:
        queue = queue[1:]
    return HttpResponse("hi")
