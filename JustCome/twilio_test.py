from twilio.rest import Client

account_sid = "AC7be8973e6f7a945d7707b14d220bb20c"

auth_token = "effe642c95803d5907f0ae04aa53fb13"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16139864968",
    from_="+18737388248",
    body="Hello!")

print(message.sid)
