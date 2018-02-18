from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Patient
import json

# Create your views here.

def home(request):
    return render(request, "waitlist/home.html")

num = 0
def enque(request):
    id = request.GET.get("patientID")
    p = request.GET.get("priority")

    print("id recevied: ", id)
    print("priority received: ", p)

    global num

    patient = Patient(patientID=id, position=num, priority=p)

    print("patient id:", patient.patientID)
    print("patient priority: ", patient.priority)
    print("patient position ", patient.position)

    num = num + 1

    p.save()

    return HttpResponseRedirect("success")

def success(request):
    return render(request, "waitlist/page.html")
