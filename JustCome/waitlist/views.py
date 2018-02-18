from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from .models import Patient
from django.urls import reverse
from twilio.rest import Client

#Authentication Information for Twili API
account_sid = "AC7be8973e6f7a945d7707b14d220bb20c"
auth_token = "effe642c95803d5907f0ae04aa53fb13"
client = Client(account_sid, auth_token)


index = 0;
def enqueue(request):
    #Get the information from the request
    id = request.GET.get("patientID")
    p = request.GET.get("priority")
    number = request.GET.get("phoneNumber")
    global index

    #Create a new patient record
    patient = Patient(patientID=id, phoneNumber=number, priority=p, index=index)
    patient.save()
    index += 1
    message = client.messages.create(
        to="+1"+number,
        from_="+18737388248",
        body="Thank you, you will be contacted when it is almost your turn.")
    return HttpResponse("Success")

def dequeue(request):
    #Get the information from the request
    number = request.GET.get("phoneNumber")

    #Filter through the database via phone number (guaranteed to be unique)
    patient = Patient.Manager.filter(phoneNumber=number)
    message = client.messages.create(
        to="+1" + patient[0].phoneNumber,
        from_="+18737388248",
        body="Someone is ready to see you now.")
    patient.delete()
    return HttpResponse("Success")

def reply(request):
    phoneNumber = request.GET.get("From")
    patient = Patient.Manager.filter(phoneNumber=phoneNumber[2:])
    count = 1;
    for patients in Patient.Manager.filter(priority=patient[0].priority):
        if (patients.index < patient[0].index):
            count += 1
    message = client.messages.create(
        to=phoneNumber,
        from_="+18737388248",
        body="You are number " + str(count) + " in line.")

def home(request):
    #Get the records for each of the priorities
    low = Patient.Manager.filter(priority="low")
    medium = Patient.Manager.filter(priority="medium")
    high = Patient.Manager.filter(priority="high")
    return render(request, "waitlist/DoctorMain1.html", {"patient_low": low, "patient_medium":medium, "patient_high":high})

def move(request):
    priority = request.GET.get("priority")
    phoneNumber = request.GET.get("phoneNumber")

    patient = Patient.Manager.filter(phoneNumber=phoneNumber).update(priority=priority)

    return HttpResponse("Response")
