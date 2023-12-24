from django.db import models
from django.contrib.auth.models import User
# Create your models here


class TypeService(models.Model):
    image=models.ImageField(upload_to="image/", default="image/default_TypeService.jpeg")
    title=models.CharField(max_length=256,default="")
    description=models.TextField(default="")




class Service(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type_service=models.ForeignKey(TypeService,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="image/", default="image/defaultService.jpg")
    title=models.CharField(max_length=256,default="")
    description=models.TextField(default="")
    initial_price=models.PositiveIntegerField(default=0)