from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskCreation(models.Model):
    title = models.CharField(max_length=300,blank=False,null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title[0:10]