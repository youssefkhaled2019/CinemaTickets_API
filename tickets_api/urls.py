from . import views
from django.urls import path,include


from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("user",views.viewsets_user)
router.register("movie",views.viewsets_movie)
router.register("reservation",views.viewsets_reservation)


urlpatterns = [
    path('', views.home), 
    #1  http://127.0.0.1:8000/no_rest0_no_model
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

    
    #7 GET POST PUT DELETE from rest framwork class based view Generics Viewsets
    # http://127.0.0.1:8000/rest_viewsets/user
    # http://127.0.0.1:8000/rest_viewsets/user/3
    
    # http://127.0.0.1:8000/rest_viewsets/movie
    # http://127.0.0.1:8000/rest_viewsets/movie/3

    # http://127.0.0.1:8000/rest_viewsets/reservation
    # http://127.0.0.1:8000/rest_viewsets/reservation/3
    path("rest_viewsets/",include(router.urls)), #api/rest/viewsets/guests
    
    #--------------------------------------------------
    #find movie  
    # http://127.0.0.1:8000/find_movie              #postman
    path("find_movie",views.find_movie),
    
    # create new reservation
    # http://127.0.0.1:8000/new_reservation             #postman
    path("new_reservation",views.new_reservation),
]
