# in this view, i will be using class based views 

from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from .models import TaskCreation
from .serializers import UserSerializer,TaskSerializers
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework.permissions import AllowAny,IsAuthenticated

class UserCreation(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self,request:Request):
        data = request.data 
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"User was created successfully",
                "data" : serializer.data
            }    
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogin(GenericAPIView):
    permission_classes = []
    queryset = User.objects.all()

    def post(self,request:Request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            print('hello')
            response = {
                "message": "Login successful",
                "Token": user.auth_token.key
            }
            return Response(data=response,status=status.HTTP_200_OK)
        else:
            response = {
                "message":"invalid email or password"
            }
            return Response(data=response,status=status.HTTP_401_UNAUTHORIZED)
        
    def get(self,request:Request):
        data = {
            "user":str(request.user),
            "auth":str(request.auth)
        }    
        print('i am working')
        return Response(data=data,status=status.HTTP_200_OK)

class TaskCreationView(GenericAPIView):
    serializer_class = TaskSerializers 
    queryset = TaskCreation.objects.all()
    permission_classes = [AllowAny]

    def post(self,request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(user = request.user)

            response = {
                "message":"Tasks was created successfully",
                "data" : serializer.data 
            }
            return Response(data=response,status=status.HTTP_201_CREATED) #returns the created data
        return Response(data=serializer.errors,status= status.HTTP_400_BAD_REQUEST) #returns bad request error 

class GetTasks(GenericAPIView):
    serializer_class = TaskSerializers
    
    def get(self,request:Request): # this view, gets all the tasks of the logged in user
        user = request.user # gets user
        task = TaskCreation.objects.filter(user=user) # filters for just users post 
        print(task)
        serializer = self.serializer_class(task, many=True)
        return Response(data={"message":serializer.data},status=status.HTTP_200_OK)