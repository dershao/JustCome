from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from .models import Patient
from django.urls import reverse
from twilio.rest import Client
import json


#Authentication Information for Twili API
account_sid = "AC7be8973e6f7a945d7707b14d220bb20c"
auth_token = "effe642c95803d5907f0ae04aa53fb13"
client = Client(account_sid, auth_token)


def enqueue(request):
    id = request.GET.get("patientID")
    p = request.GET.get("priority")
    number = request.GET.get("phoneNumber")

    patient = Patient(patientID=id, phoneNumber=number, priority=p)
    patient.save()
    return HttpResponse({id:1})

def dequeue(request):
    number = request.GET.get("phoneNumber")
    patient = Patient.Manager.filter(phoneNumber=number)
    message = client.messages.create( to="+1" + patient[0].phoneNumber, from_="+18737388248", body="I love you")
    patient.delete()
    return HttpResponse({id:1})

def home(request):
    low = Patient.Manager.filter(priority="low")
    medium = Patient.Manager.filter(priority="medium")
    high = Patient.Manager.filter(priority="high")

    return render(request, "waitlist/DoctorMain.html", {"patient_low": low, "patient_medium":medium, "patient_high":high})
