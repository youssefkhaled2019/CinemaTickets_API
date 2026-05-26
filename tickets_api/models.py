from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class Movie(models.Model):
    movie =models.CharField(max_length=50)
    hall=models.CharField(max_length=20)#choices=h
    date=models.DateField(null=True, blank=True)
  
    def __str__(self):
        return self.movie
    
class Guest(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)


    def __str__(self):
        return self.name



class Reservation(models.Model):
    user=models.ForeignKey(Guest,related_name="reservation",on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,related_name="reservation",on_delete=models.CASCADE)


#================================= 
    



class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50 )
    body=models.TextField()

    def __str__(self):
        return self.author.username
#------------------------------------

@receiver(post_save,sender=User)
def TokenCreate(sender,instance,created,**Kwargs):
    if created:
        Token.objects.create(user=instance)
