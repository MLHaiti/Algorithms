from queue import Queue

# we can use queue for task scheduling
# for example to send sms in the good order
messageToSent = Queue()

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

messageToSent.enqueue(sms_1)
messageToSent.enqueue(sms_2)
messageToSent.enqueue(sms_3)

# sending the first message first
print(f"sending ... : {messageToSent.dequeue()}")
print(f"sending ... : {messageToSent.dequeue()}")
print(f"sending ... : {messageToSent.dequeue()}")
