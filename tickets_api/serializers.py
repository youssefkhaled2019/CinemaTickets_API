from rest_framework import serializers
from .models import Movie,Guest,Reservation,Post


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class UserSerializers(serializers.ModelSerializer):
    mobile = serializers.RegexField(regex=r'^01[0-9]{9}$', error_messages={"invalid": "Invalid mobile number (must start with 01 and be 11 digits)" })
    class Meta:
        model=Guest
        fields=["pk","reservation","name","mobile"]  
        extra_kwargs = {'reservation': {'read_only': True}}# 'required': True

    # validate
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        if Guest.objects.filter(name=value.strip()).exists() :
            raise serializers.ValidationError("Name  is used")
        return value

    def validate_mobile(self, value):
        if not value.strip():
            raise serializers.ValidationError("Mobile cannot be empty")

        if not value.isdigit():
            raise serializers.ValidationError("Mobile must be numbers only")

        if len(value) < 10:
            raise serializers.ValidationError("Mobile too short")

        return value
  
class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'   


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["pk","title","body"]
        read_only_fields = ['author']       

