from django.http import HttpResponse,JsonResponse 
from .models import Move,User,Reservation
from  rest_framework.decorators import api_view
from .serializers import MoveSerializers ,UserSerializers,ReservationSerializers
from  rest_framework.response import Response
from  rest_framework import status ,filters
# Create your views here.
def home(request):
    return HttpResponse("ddddd")

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
    data=User.objects.all()

    #data=list(data.values())   #1
    data={"data":list(data.values("name","mobile")) } #2

    return JsonResponse(data) #safe=False #1

#function based views
#3.1 GET POST
@api_view(["GET","POST"])
def fbv_user(request):
    if request.method=="GET":
      data=User.objects.all()
      serializer=UserSerializers(data,many=True)
      return Response(serializer.data)
    if request.method=="POST":
       serializer=UserSerializers(data=request.data)
       if(serializer.is_valid()):
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       return Response({"message":"error"},status=status.HTTP_400_BAD_REQUEST)
       #return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

#function based views
#3.2 GET PUT DELETE
@api_view(["GET","PUT","DELETE"])
def fbv_user_id(request,id):
    try:
        data=User.objects.get(id=id)
    except User.DoesNotExist   :
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
