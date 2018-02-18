from django.shortcuts import render
from django.http import HttpResponse
#from .models import Patient
from twilio.rest import Client

account_sid = "AC7be8973e6f7a945d7707b14d220bb20c"
auth_token = "effe642c95803d5907f0ae04aa53fb13"
client = Client(account_sid, auth_token)




queue = []

# Create your views here.
def queue(request):
    return render(request, 'waitlist/page.html')

def data(request):
    increment = request.POST.get("delta")
    if (increment == 1):
        queue.append(1)
    else:
        queue = queue[1:]
    return HttpResponse("hi")

def dequeue(request):
	message = client.messages.create( to="+16139864968", from_="+18737388248", body="Please work")
	return HttpResponse("Please Work")

