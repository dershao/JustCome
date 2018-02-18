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

from django.http import HttpResponse
#from .models import Patient
from twilio.rest import Client

account_sid = "AC7be8973e6f7a945d7707b14d220bb20c"
auth_token = "effe642c95803d5907f0ae04aa53fb13"
client = Client(account_sid, auth_token)

def dequeue(request):
	message = client.messages.create( to="+16139864968", from_="+18737388248", body="Please work")
	return HttpResponse("Please Work")
