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



class Review(models.Model):
    services=models.ForeignKey(Service, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    rating= models.IntegerField(default=0)
    comment=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}"
