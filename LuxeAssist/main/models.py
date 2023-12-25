from django.db import models
from django.contrib.auth.models import User
from request.models import  Request
# Create your models here.


class Payment(models.Model):
   categories= models.TextChoices("categories", ["Bank Card" ,"pay made ","App pay"])


   user=models.ForeignKey(User, on_delete=models.CASCADE)
   requests=models.ForeignKey(Request, on_delete=models.CASCADE)
   method_card= models.CharField(max_length=70, choices=categories.choices,default="Cultural")
   full_name= models.CharField(max_length=2048)
   number_card= models.PositiveIntegerField()
   expiration_date =models.DateField()
   cvv=models.PositiveIntegerField()

  
   def __str__(self):
     
     return f"{self.full_name}" 
   

class Contact(models.Model):
      
  categories= models.TextChoices("categories", ["Suggestion" ,"Complaint"])
      
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  type=models.CharField(max_length=70, choices=categories.choices,default="Cultural")
  content=models.TextField()

      
  def __str__(self):
        
    return f"{self.type}"