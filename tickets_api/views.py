
from django.shortcuts import redirect #,render,
from django.contrib.auth import logout#,authenticate,login,
from django.http import HttpResponse,JsonResponse ,Http404
# from django.http.response import JsonResponse,HttpResponse
from .models import Movie,Guest,Reservation,Post
from  rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import MovieSerializers ,UserSerializers,ReservationSerializers,PostSerializers
from  rest_framework.response import Response
from  rest_framework import status ,filters ,generics,mixins,viewsets,permissions
from rest_framework.views import APIView
# from django_filters.rest_framework import DjangoFilterBackend
#----------------
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
#----------------
from .permissions import IsAuthorOrReadOnly ,IsAuthor
#----------------
from django.views.decorators.csrf import csrf_exempt
#----------------
def home(request):
    return HttpResponse("api")
#----------------

# -------------------- pagination --------------------
from rest_framework.pagination import PageNumberPagination
class MyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  
    max_page_size = 100

#----------------


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

#----------------

#2 model data defoult django without REST
def no_rest_from_model(request):
    data=Guest.objects.all()
    data={"data":list(data.values("name","mobile")) }
    return JsonResponse(data) 


#----------------
#function based views
#3.1 GET POST
@api_view(["GET","POST"])
def fbv_user(request):
    if request.method=="GET": 
        data=Guest.objects.all()
        paginator = MyPagination()
        page = paginator.paginate_queryset(data, request) 
        serializer = UserSerializers(page, many=True)  
        return paginator.get_paginated_response(serializer.data) 
    if request.method=="POST":
       serializer=UserSerializers(data=request.data)
       if(serializer.is_valid(raise_exception=True)):
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response({"message":"error"+str(serializer.errors)},status=status.HTTP_400_BAD_REQUEST)

#function based views
#3.2 GET PUT DELETE
@api_view(["GET","PUT","DELETE"])
def fbv_user_id(request,id):
    try:
        data=Guest.objects.get(id=id)
    except Guest.DoesNotExist   :
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
   
#----------------

#CBV class based views
#4.1 list and create  -> GET POST
class CBV_List(APIView): 
    def get(self,request):
         guests=Guest.objects.all()
         serializer=UserSerializers(guests,many=True)
         return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(  {  "success": False,  "errors": serializer.errors },status=status.HTTP_400_BAD_REQUEST)



#4.2 GET PUT DELETE cloass based views  -> pk
class CBV_pk(APIView):
    
    def get_object(self,pK):
          try:
             return Guest.objects.get(id=pK)
          except Guest.DoesNotExist :
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
        return Response(  {  "success": False,  "errors": serializer.errors },status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pK):
        guest=self.get_object(pK)
        guest.delete()
        response={"message":"delete data "}
        return Response(response,status=status.HTTP_204_NO_CONTENT)
#----------------


#5 Mixins don't repeat yourself
#5.1 mixins list
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset =Guest.objects.all() 
    serializer_class=UserSerializers  
    # pagination_class = MyPagination

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
  
    


#5.2 mixins GET PUT DELETE      
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset =Guest.objects.all()
    serializer_class=UserSerializers
            
    def get(self,request,pk):
        return self.retrieve(request)  #RetrieveModelMixin for return  one element
    def put(self,request,pk):
        return self.update(request) 
    def delete(self,request,pk):
        return self.destroy(request)  # If an object is deleted this returns a 204 No Content response, otherwise it will return a 404 Not Found.
        # instance = self.get_object()
        # self.perform_destroy(instance)
        # response={"message":"delete data "}
        # return Response(response,status=status.HTTP_204_NO_CONTENT)   
    
#----------------
    
#6 Generics

#6.1 GET and POST
class generics_list(generics.ListCreateAPIView):#ListCreateAPIView ,ListAPIView
    queryset =Guest.objects.all()
    serializer_class=UserSerializers
    pagination_class = MyPagination
    #======================-Basic=======================
    # authentication_classes=[BasicAuthentication] 
    # permission_classes=[IsAuthenticated]
    #=====================Tocken========================
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    #=============================================
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

#6.2 GET PUT DELETE  
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset =Guest.objects.all()
    serializer_class=UserSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response={"message":"delete data "}
        return Response(response,status=status.HTTP_204_NO_CONTENT)
    
    # def get(self, request, *args, **kwargs):
    #      return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

#----------------

    

#7  Viewsets  ALL 
class viewsets_user(viewsets.ModelViewSet):
    queryset =Guest.objects.all()
    serializer_class=UserSerializers
    pagination_class = MyPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response={"message":"delete data "}
        return Response(response,status=status.HTTP_204_NO_CONTENT)
    

class viewsets_movie(viewsets.ModelViewSet):
    #  authentication_classes=[BasicAuthentication]
    #  permission_classes=[IsAuthenticated]
    #-------------------Tocken-------------------
    #  authentication_classes=[TokenAuthentication]
    #  permission_classes=[IsAuthenticated]#[IsAuthenticated,AllowAny]
     queryset =Movie.objects.all()
     serializer_class=MovieSerializers
     pagination_class = MyPagination
     def destroy(self, request, *args, **kwargs):
        response={"message":"delete data "}
        return Response(response,status=status.HTTP_204_NO_CONTENT)

    

    #=============================================
    #  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    #  filterset_fields = ["hall"]
    #  search_fields = ["name"]
     
    #  filter_backend=[DjangoFilterBackend,filters.SearchFilter,]
    #  filterset_fields = ["name",]
    #  search_fields=["name",]

    #  def get_queryset(self):
    #     queryset = self.queryset
    # company_id = self.request.query_parameters.get('company', None)
    #     query_set = queryset.filter(user=self.request.user)
    #     return query_set

class viewsets_reservation(viewsets.ModelViewSet):
     
     queryset =Reservation.objects.all()
     serializer_class=ReservationSerializers
     pagination_class = MyPagination
#----------------
#8 find movie     by  function based views
@api_view(["GET"])  #postman 
def find_movie(request):
    # print(request.data)
    # movies=Movie.objects.filter(movie=request.data["movie"],hall=request.data["hall"])
    movies=Movie.objects.filter(movie__contains=request.data["movie"]) #request.data["movie"]
     
    serializer=MovieSerializers(movies,many=True)
    return Response(serializer.data)
#----------------

# 9-create new reservation
@api_view(["POST"])  #postman 
def new_reservation(request):
  
    try:
        movie=Movie.objects.get(movie__contains=request.data["movie"])#hall=request.data["hall"]


    except :
        return  Response({"message":"movie not found"},status=status.HTTP_201_CREATED)


    serializer=UserSerializers(data={"name":request.data["name"],"mobile":request.data["mobile"]})
    if(serializer.is_valid(raise_exception=True)): #<---- validate
           guest=serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)

    reservation=Reservation()
    reservation.user=guest
    reservation.movie=movie
    reservation.save()

    serializer =ReservationSerializers(reservation)


    return Response(serializer.data,status=status.HTTP_201_CREATED)


# 9-create new reservation
@api_view(["POST"])  #postman 
def new_reservation2(request):
  
    try:
        movie=Movie.objects.get(movie__contains=request.data["movie"])#hall=request.data["hall"]


    except :
        return  Response({"message":"movie not found"},status=status.HTTP_201_CREATED)
    try:
            guest=Guest()
            guest.name=request.data["name"]
            guest.mobile=request.data["mobile"]
            guest.save()
            
    except :
        return  Response({"message":"user error"},status=status.HTTP_201_CREATED)



    reservation=Reservation()
    reservation.user=guest
    reservation.movie=movie
    reservation.save()

    serializer =ReservationSerializers(reservation)


    return Response(serializer.data,status=status.HTTP_201_CREATED)
#-------------------------------------------------
class Post_List(generics.ListCreateAPIView):
     authentication_classes=[TokenAuthentication]
     permission_classes=[IsAuthenticated]#IsAuthenticated    
     queryset=Post.objects.all()
     serializer_class=PostSerializers
     def post(self, request, *args, **kwargs):


        serializer=PostSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        # return self.update(request, *args, **kwargs)



class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    #  authentication_classes=[TokenAuthentication] #BasicAuthentication
     permission_classes=[IsAuthorOrReadOnly]#IsAuthorOrReadOnly,IsAuthor,IsAuthenticated
     queryset=Post.objects.all()
     serializer_class=PostSerializers



#----------------


class LogoutView(APIView):
    """
    Djano 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect('/')

#---------------------A-----------------------------
     

