from django.contrib import admin
from .models import Move,User,Reservation

# Register your models here.
admin.site.register(Move)
admin.site.register(User)
admin.site.register(Reservation)