from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('register/',views.UserCreation.as_view(),name='registerUser'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('',views.GetAllLinks.as_view(),name= "allLinks"),
    path('createTask/',views.TaskCreationView.as_view(),name="createTask"),
    path('getTask/',views.GetTasks.as_view(),name="getTask"),
    path('task/<int:id>',views.GetUpdateDeleteTask.as_view(),name='tasks'),
]
