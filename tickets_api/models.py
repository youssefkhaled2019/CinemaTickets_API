from django.db import models

# Create your models here.

# h=[("A01","A01"),
#    ("A02","A02"),
#    ("A03","A03"),
#    ("A04","A04"),]

# t=[("3-6","3-6"),
#    ("6-9","6-9"),
#    ("9-12","9-12"),]

class Move(models.Model):
    name =models.CharField(max_length=50)
    hall=models.CharField(max_length=20)#choices=h
    time=models.DateField()
    # time=models.CharField(max_length=20,choices=t ,default=t[0])
    def __str__(self):
        return self.name
    
class User(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Reservation(models.Model):
    user=models.ForeignKey(User,related_name="reservation",on_delete=models.CASCADE)
    move=models.ForeignKey(Move,related_name="reservation",on_delete=models.CASCADE)