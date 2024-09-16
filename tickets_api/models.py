from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

# h=[("A01","A01"),
#    ("A02","A02"),
#    ("A03","A03"),
#    ("A04","A04"),]

# t=[("3-6","3-6"),
#    ("6-9","6-9"),
#    ("9-12","9-12"),]

class Movie(models.Model):
    movie =models.CharField(max_length=50)
    hall=models.CharField(max_length=20)#choices=h
    time=models.DateField()
    # time=models.CharField(max_length=20,choices=t ,default=t[0])
    def __str__(self):
        return self.movie
    
class User2(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    user=models.ForeignKey(User2,related_name="reservation",on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,related_name="reservation",on_delete=models.CASCADE)


#=================================
    



#------------------------------------
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50 )
    body=models.TextField()


# #------------------------------------

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
@receiver(post_save,sender=User)
def TokenCreate(sender,instance,created,**Kwargs):
    if created:
        Token.objects.create(user=instance)
