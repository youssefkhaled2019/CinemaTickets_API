from django.contrib import admin
from .models import Movie,User,Reservation

# Register your models here.
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Reservation)