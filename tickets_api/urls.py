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
    #1  http://127.0.0.1:8000/no_rest_no_model
    path("no_rest_no_model",views.no_rest_no_model),

    #2  http://127.0.0.1:8000/no_rest_from_model
    path("no_rest_from_model",views.no_rest_from_model),

    #3.1 GET POST from rest framwork function based view @api_view
    #  http://127.0.0.1:8000/fbv_user
    path("fbv_user",views.fbv_user),
    #3.2 GEY PUT DELETE from rest framwork function based view @api_view
    #  http://127.0.0.1:8000/fbv_user_id/1
    path("fbv_user_id/<int:id>",views.fbv_user_id),

    #4.1  GET POST  from rest framwork class based view APIView
    #  http://127.0.0.1:8000/rest_cbv/
    path("rest_cbv/",views.CBV_List.as_view()),
    #4.2 GEY PUT DELETE from rest framwork class based view APIView
    #  http://127.0.0.1:8000/rest_cbv/1
    path("rest_cbv/<int:pK>",views.CBV_pk.as_view()),


    #5.1  GET POST  from rest framwork class based view Mixins
    # http://127.0.0.1:8000/rest_mixins/
    path("rest_mixins/",views.mixins_list.as_view()),
    #5.2  GEY PUT DELETE from rest framwork class based view Mixins
    # http://127.0.0.1:8000/rest_mixins/1
    path("rest_mixins/<int:pk>",views.mixins_pk.as_view()),

    #6.1  GET POST  from rest framwork class based view Generics
    # http://127.0.0.1:8000/rest_generics/
    path("rest_generics/",views.generics_list.as_view()),
    #6.2  GEY PUT DELETE from rest framwork class based view Generics
    # http://127.0.0.1:8000/rest_generics/1
    path("rest_generics/<int:pk>",views.generics_pk.as_view()),

    
    #7.1 GET POST PUT DELETE from rest framwork class based view Generics Viewsets
    # http://127.0.0.1:8000/rest_viewsets/user/
    # http://127.0.0.1:8000/rest_viewsets/user/3
    # 7.2
    # http://127.0.0.1:8000/rest_viewsets/movie/
    # http://127.0.0.1:8000/rest_viewsets/movie/3
     # 7.3
    # http://127.0.0.1:8000/rest_viewsets/reservation/
    # http://127.0.0.1:8000/rest_viewsets/reservation/3
    path("rest_viewsets/",include(router.urls)), #api/rest/viewsets/guests



    #8- find movie  
    # http://127.0.0.1:8000/find_movie              
    path("find_movie",views.find_movie),

    # create new reservation
    # http://127.0.0.1:8000/new_reservation             #postman ->get->body->x-www-form-urlencoded -> your pramter
    path("new_reservation",views.new_reservation),

    # ===============================================================
    #logout
    # path('api-auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls')),  #notwork
    #token authentication
    

 
       
   #Token Authentication
    # http://127.0.0.1:8000/api-token-auth/
    path('api-token-auth/',obtain_auth_token),   #                        Authorization , Token b4662b832ac7f404c3bf3c332ef33e8ca33e3a39

    #--------------------------------------------------

    



  


    # http://127.0.0.1:8000/rest_post_generics
     path("rest_post_generics",views.Post_List.as_view()),
    # http://127.0.0.1:8000/rest_post_generics/2
    path("rest_post_generics/<int:pk>",views.Post_pk.as_view()),
 ]
