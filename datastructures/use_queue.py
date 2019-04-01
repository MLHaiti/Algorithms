from queue import Queue

# we can use queue for task scheduling
# for example to send sms in the good order
smsToSend = Queue()

sms_1 = {
    'id': 1,
    'to': 48085184,
    'body': "votre rendez-vous est validé"
}

sms_2 = {
    'id': 2,
    'to': 48085184,
    'body': "Le docteur annonce un changement dans l'heure"
}

sms_3 = {
    'id': 2,
    'to': 48085184,
    'body': "Rappel de votre rendez-vous ce dimanche"
}

smsToSend.enqueue(sms_1)
smsToSend.enqueue(sms_2)
smsToSend.enqueue(sms_3)

# sending the first message first written each time
print(f"sending ... : {smsToSend.dequeue()}")
print(f"sending ... : {smsToSend.dequeue()}")
print(f"sending ... : {smsToSend.dequeue()}")
