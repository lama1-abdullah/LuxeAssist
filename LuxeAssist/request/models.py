from django.db import models
from django.contrib.auth.models import User
from services.models import Service

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status_type = models.TextChoices("Status", ["Pending", "Approve", "Reject", "Cancle"])
    note = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(max_length = 1024, choices = status_type.choices, default = "pending")
    request_price = models.PositiveIntegerField()

class RequestComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requests= models.ForeignKey(Request, on_delete=models.CASCADE)
    comment = models.TextField()


