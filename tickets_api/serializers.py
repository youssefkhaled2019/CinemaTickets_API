from rest_framework import serializers
from .models import Movie,User,Reservation



# uuid - slug   
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["pk","reservation","name","mobile"]    

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'   