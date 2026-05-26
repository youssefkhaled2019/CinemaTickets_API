from . import views
from django.urls import path,include

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("user",views.viewsets_user)
router.register("movie",views.viewsets_movie)
router.register("reservation",views.viewsets_reservation)


urlpatterns = [
    path('', views.home), 
    path("no_rest_no_model",views.no_rest_no_model),
    path("no_rest_from_model",views.no_rest_from_model),
    path("fbv_user",views.fbv_user),
    path("fbv_user_id/<int:id>",views.fbv_user_id),
    path("rest_cbv/",views.CBV_List.as_view()),
    path("rest_cbv/<int:pK>",views.CBV_pk.as_view()),
    path("rest_mixins/",views.mixins_list.as_view()),
    path("rest_mixins/<int:pk>",views.mixins_pk.as_view()),
    path("rest_generics/",views.generics_list.as_view()),
    path("rest_generics/<int:pk>",views.generics_pk.as_view()),
    path("rest_viewsets/",include(router.urls)),    
    path("find_movie",views.find_movie), 
    path("new_reservation",views.new_reservation),
    path('api-auth', include('rest_framework.urls')),
    
    #Token Authentication
    # http://127.0.0.1:8000/api-token-auth/                   {"username": "youssef","password": "youssef"}
    path('api-token-auth/',obtain_auth_token),   #                        Authorization , Token b4662b832ac7f404c3bf3c332ef33e8ca33e3a39

    # http://127.0.0.1:8000/rest_post_generics
    path("rest_post_generics",views.Post_List.as_view()),
    # http://127.0.0.1:8000/rest_post_generics/2
    path("rest_post_generics/<int:pk>",views.Post_pk.as_view()),
 ]
