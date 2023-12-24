from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="image/" , default="image/default.png",blank=True)
    city = models.CharField(max_length=255 , default="Riyadh")
    address = models.CharField(max_length=255 , default="Riyadh")
    phone_number = models.IntegerField()

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')

    nationality = models.CharField(max_length=255 , default="Saudi")
    about = models.TextField()

    def __str__(self) :
        return f"{self.user.first_name} profile"