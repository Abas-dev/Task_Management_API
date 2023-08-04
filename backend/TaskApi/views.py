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
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class PaginationClass(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4

class GetAllLinks(GenericAPIView):
    permission_classes = []

    def get(self,request:Request):
        response = {
            "homeRoute" : "localhost:8000/",
            "register(POST)" : "localhost:8000/register/",
            "login(POST)" : "localhost:8000/login/",
            "createTask(POST)" : "localhost:8000/createTask/",
            "getTask(GET)": "localhost:8000/getTask/",
            "getTaskById(GET)" : "localhost:8000/task/{id}",
            "updateTaskByid(PUT)" : "localhost:8000/task/{id}",
            "deleteTaskById(DELETE)" : "localhost:8000/task/{id}",
        }   
        return Response(data=response,status=status.HTTP_200_OK)

class UserCreation(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []

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
        username = request.data.get('username') # gets username
        password = request.data.get('password') # get password

        user = authenticate(request,username=username,password=password) # authenticates username and password
        
        if user is not None: # checks if user is not none

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
    permission_classes = [IsAuthenticated]

    def post(self,request:Request):
        data = request.data # gets the data 
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(): # check if data is valid 
            serializer.save(user = request.user)

            response = {
                "message":"Tasks was created successfully",
                "data" : serializer.data # sends data in json
            }
            return Response(data=response,status=status.HTTP_201_CREATED) #returns the created data
        return Response(data=serializer.errors,status= status.HTTP_400_BAD_REQUEST) #returns bad request error 

class GetTasks(GenericAPIView):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationClass

    def get(self,request:Request): # this view, gets all the tasks of the logged in user
        user = request.user # gets user
        task = TaskCreation.objects.filter(user=user) # filters for just users task
        page = self.paginate_queryset(task)
        serializer = self.serializer_class(page, many=True)

        response = {
            "message":serializer.data
        }

        return Response(data=response,status=status.HTTP_200_OK)
    

class GetUpdateDeleteTask(GenericAPIView):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]

    def get(self,request:Request,id):
        data = get_object_or_404(TaskCreation,id=id)
        serializer = self.serializer_class(instance=data)
        return Response(data={"message":serializer.data},status=status.HTTP_200_OK)

    def put(self,request:Request,id):
        data_id = get_object_or_404(TaskCreation,id=id) # gets the id of thr class
        data = request.data # get data 
        serializer = self.serializer_class(instance=data_id,data=data) # gets the data and updates it 

        if serializer.is_valid():
            serializer.save() # saves data 

            response = {
                "message" : "data updated successfully",
                "data" : serializer.data # returns the data 
            }

            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=response,status=status.HTTP_201_CREATED)

    def delete(self,request:Request,id):
        data_id = get_object_or_404(TaskCreation,id=id) # gets the data by it id
        data_id.delete()
        response = {
            "message":"data was deleted successfully"
        }
        return Response(data=response,status=status.HTTP_204_NO_CONTENT)

