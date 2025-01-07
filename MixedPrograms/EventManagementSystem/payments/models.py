from django.db import models
from events.models import Event
from django.contrib.auth.models import User

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

