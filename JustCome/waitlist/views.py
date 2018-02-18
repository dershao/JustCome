from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Patient
from twilio.rest import Client
import json


#Authentication Information for Twili API
account_sid = "AC7be8973e6f7a945d7707b14d220bb20c"
auth_token = "effe642c95803d5907f0ae04aa53fb13"
client = Client(account_sid, auth_token)

def home(request):
    low = Patient.Manager.filter(priority="low")

    return render(request, "waitlist/JustCome.html", {"patient_low": low})

num = head = 0
def enqueue(request):
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
    patient.save()
    return HttpResponseRedirect("home")

def dequeue(request):
	global head
	patient = Patient.Manager.filter(position=head)
	message = client.messages.create( to="+1" + patient[0].patientID, from_="+18737388248", body="Hello I hate you")
	patient.delete()
	head = head + 1;
	return HttpResponse("Please Work")

def nurse(request):
    low = Patient.Manager.filter(priority="low")

    return render(request, "waitlist/NurseMain.html", {"patient_low": low})
