from rest_framework import serializers
from .models import TaskCreation
from django.contrib.auth.models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 50)
    email = serializers.CharField(max_length = 50)
    password = serializers.CharField(min_length = 8,write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',  
        ]
        
    def validate(self, attrs):
        email_exist = User.objects.filter(email=attrs['email']).exists()

        if email_exist:
            raise ValidationError("email already exist")

        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

class TaskSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = TaskCreation 
        fields = ['id','user','title','description']       