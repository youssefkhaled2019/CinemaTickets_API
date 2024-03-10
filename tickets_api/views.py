
from django.shortcuts import redirect #,render,
from django.contrib.auth import logout#,authenticate,login,
from django.http import HttpResponse,JsonResponse ,Http404
from .models import Movie,User2,Reservation,Post
from  rest_framework.decorators import api_view
from .serializers import MovieSerializers ,UserSerializers,ReservationSerializers,PostSerializers
from  rest_framework.response import Response
from  rest_framework import status ,filters ,generics,mixins,viewsets,permissions
from rest_framework.views import APIView
#----------------
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#----------------
from .permissions import IsAuthorOrReadOnly 
#----------------
# from django_filters.rest_framework import DjangoFilterBackend
#----------------

# Create your views here.
def home(request):
    return HttpResponse("api")

#1 without REST and no mode query FBV
def  no_rest_no_model(request):

    data=[
        {
            "id":1,
            "name":"omer",
            "mobile":102536947,
        }, 
        {
            "id":2,
            "name":"nader",
            "mobile":157755789,
        }
    ]
    return JsonResponse(data,safe=False)  #data without huch


#2 model data defoult django without REST
def no_rest_from_model(request):
    data=User2.objects.all()

    #data=list(data.values())   #1
    data={"data":list(data.values("name","mobile")) } #2

    return JsonResponse(data) #safe=False #1

# LIST =GET
# CREARTE =POST

# PK QURE=GET
# UPDATE=PUT
# DELETE=DELETE

#function based views
#3.1 GET POST
@api_view(["GET","POST"])
def fbv_user(request):
    if request.method=="GET":
      data=User2.objects.all()
      serializer=UserSerializers(data,many=True)
      return Response(serializer.data)
    if request.method=="POST":
       serializer=UserSerializers(data=request.data)
       if(serializer.is_valid()):
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response({"message":"error"},status=status.HTTP_400_BAD_REQUEST)#serializer.data
    

#function based views
#3.2 GET PUT DELETE
@api_view(["GET","PUT","DELETE"])
def fbv_user_id(request,id):
    try:
        data=User2.objects.get(id=id)
    except User2.DoesNotExist   :
        response={"message":"not found"}
        return Response(response,status=status.HTTP_404_NOT_FOUND)
       
    if request.method=="GET":
     
      serializer=UserSerializers(data)
      return Response(serializer.data)
    
    if request.method=="PUT":
       serializer=UserSerializers(data,data=request.data)
       if(serializer.is_valid()):
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)

       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        data.delete()
        response={"message":"delete data "}
        return Response(response,status=status.HTTP_204_NO_CONTENT)
    

#CBV class based views
#4.1 list and create  -> GET POST
class CBV_List(APIView):
    def get(self,request):#two pramter
         guests=User2.objects.all()
         serializer_=UserSerializers(guests,many=True) #x serializer
         return Response(serializer_.data)
    def post(self,request):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)



#4.2 GET PUT DELETE cloass based views  -> pk
class CBV_pk(APIView):
    
    
    def get_object(self,pK): #x  get_object
          try:
             return User2.objects.get(id=pK)
          except User2.DoesNotExist :
            raise Http404

       
    def get(self,request,pK):
        
        guest=self.get_object(pK) 
        serializer= UserSerializers(guest)
        return Response(serializer.data)

    def put(self,request,pK):
        guest=self.get_object(pK)
        serializer= UserSerializers(guest,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)#,status=status.HTTP_201_CREATED
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
    def delete(self,request,pK):
           guest=self.get_object(pK)
           guest.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)


#5 Mixins don't repeat yourself
#5.1 mixins list
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset =User2.objects.all() #X queryset
    serializer_class=UserSerializers  #X serializer_class
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)


#5.2 mixins GET PUT DELETE      
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset =User2.objects.all()
    serializer_class=UserSerializers
                                          
    def get(self,request,pk):
        return self.retrieve(request)  #RetrieveModelMixin for return  one element
    def put(self,request,pk):
        return self.update(request) 
    def delete(self,request,pk):
        return self.destroy(request)    
    
#6 Generics

#6.1 GET and POST
class generics_list(generics.ListCreateAPIView):#ListCreateAPIView ,ListAPIView
    queryset =User2.objects.all()
    serializer_class=UserSerializers
    #======================-Basic=======================
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    #=====================Tocken========================
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

#6.2 GET PUT DELETE  
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset =User2.objects.all()
    serializer_class=UserSerializers
    #=============================================
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
   #-------------------Tocken-------------------
    authentication_classes=[TokenAuthentication]

    

#7  Viewsets  ALL 
class viewsets_user(viewsets.ModelViewSet):
    queryset =User2.objects.all()
    serializer_class=UserSerializers
    #=============================================
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]






class LogoutView(APIView):
    """
    Djano 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect('/')

#---------------------A-----------------------------
     

class viewsets_movie(viewsets.ModelViewSet):
     
     queryset =Movie.objects.all()
     serializer_class=MovieSerializers

    #  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    #  filterset_fields = ["hall"]
    #  search_fields = ["name"]
     
     filter_backend=[filters.SearchFilter]
     search_fields=["name"]






class viewsets_reservation(viewsets.ModelViewSet):
     queryset =Reservation.objects.all()
     serializer_class=ReservationSerializers

#-------------------------B-------------------------
 #8 find movie     by  function based views
@api_view(["GET"])  #postman 
def find_movie(request):

    # movies=Movie.objects.filter(movie=request.data["movie"],hall=request.data["hall"])
    movies=Movie.objects.filter(movie__contains=request.data["movie"]) 
     
    serializer=MovieSerializers(movies,many=True)
    return Response(serializer.data)

# create new reservation
@api_view(["POST"])  #postman 
def new_reservation(request):
  
    movie=Movie.objects.get(movie=request.data["movie"],hall=request.data["hall"])
    guest=User2()
    guest.name=request.data["name"]
    guest.mobile=request.data["mobile"]
    guest.save()

    reservation=Reservation()
    reservation.user=guest
    reservation.movie=movie
    reservation.save()

    serializer =ReservationSerializers(reservation)


    return Response(serializer.data,status=status.HTTP_201_CREATED)
#-------------------------------------------------
class Post_List(generics.ListCreateAPIView):
     permission_classes=[IsAuthorOrReadOnly]
     queryset=Post.objects.all()
     serializer_class=PostSerializers

class Post_pk(generics.RetrieveUpdateDestroyAPIView):
     permission_classes=[IsAuthorOrReadOnly]
     queryset=Post.objects.all()
     serializer_class=PostSerializers