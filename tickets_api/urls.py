from . import views
from django.urls import path

urlpatterns = [
    path('', views.home), 
     #1  http://127.0.0.1:8000/no_rest_no_model
    path("no_rest_no_model",views.no_rest_no_model),
     #2  http://127.0.0.1:8000/no_rest_from_model
    path("no_rest_from_model",views.no_rest_from_model),
    #3.1 GET POST from rest framwork function based view @api_view
    #http://127.0.0.1:8000/fbv_user
    path("fbv_user",views.fbv_user),
    #3.2 GEY PUT DELETE from rest framwork function based view @api_view
    #http://127.0.0.1:8000/fbv_user_id/1
    path("fbv_user_id/<int:id>",views.fbv_user_id),
]
