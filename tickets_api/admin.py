from django.contrib import admin
from .models import Movie,User2,Reservation,Post

# Register your models here.
admin.site.register(Movie)
admin.site.register(User2)
admin.site.register(Reservation)
admin.site.register(Post)