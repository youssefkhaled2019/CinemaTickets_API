from rest_framework import serializers
from .models import Movie,User2,Reservation,Post



# uuid - slug   
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User2
        fields=["pk","reservation","name","mobile"]    

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'   


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'         