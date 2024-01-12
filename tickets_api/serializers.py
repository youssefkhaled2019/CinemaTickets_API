from rest_framework import serializers
from .models import Move,User,Reservation



# uuid - slug   
class MoveSerializers(serializers.ModelSerializer):
    class Meta:
        model=Move
        fields='__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["pk","reservation","name","mobile"]    

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'   