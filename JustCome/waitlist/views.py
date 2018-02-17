from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def queue(request):
    return render(request, 'waitlist/page.html')
