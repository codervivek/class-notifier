from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Student(models.Model):

    user=models.OneToOneField(User,help_text="a",related_name='student',on_delete=models.CASCADE)

    department=models.CharField(max_length=100,help_text="Enter your department")

    mail=models.CharField(max_length=200, help_text="@iitg.ernet.in", blank=True, null=True)

    phone=models.CharField(max_length=200, help_text="Enter your contact no.", blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('notification_list')

class Notification(models.Model):

    user=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    text=models.CharField(max_length=200)

    created_date = models.DateTimeField(default=timezone.now)