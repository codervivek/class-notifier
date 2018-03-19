__author__ = "Vivek Raj, Kapil Goyal and Rohit Pant"
__credits__ = ["Nitin Kedia", "Jatin Goyal", "Sahib Khan",
                    "Sparsh Bansal"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Vivek Raj"
__email__ = "raj.vivek.151297@gmail.com"
__status__ = "Development"

# import other libraries
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Following are models:

# Student is an entity object which contains attributes and methods which define a student in our context
class Student(models.Model):
    # This attribute defines a one to one relationship with predefined User class.
    # It contains Username, Password, First name and Last name.
    user=models.OneToOneField(User,help_text="a",related_name='student',on_delete=models.CASCADE)

    # A string field which defines the department of the student.
    department=models.CharField(max_length=100,help_text="Enter your department")

    # A string field which defines webmail of the student
    mail=models.CharField(max_length=200, help_text="@iitg.ernet.in", blank=True, null=True)

    # A string field which defines the phone no. of the student
    phone=models.CharField(max_length=200, help_text="Enter your contact no.", blank=True, null=True)

    # A method which gives a name to a student object
    def __str__(self):
        return self.user.username

    # A method which gives url to the given student object
    def get_absolute_url(self):
        return reverse('notification_list')

# Notification is an entity object. It contains timestamp (the time at which notification was sent)
# and a string field which defines the text in the notification.
class Notification(models.Model):

    # It defines a composition relationship between a student object and notification object
    # ( Student object is leader and notification objects are delegates )s
    user=models.ForeignKey(Student,on_delete=models.CASCADE)

    # a string field which defines the text in the notification.
    text=models.CharField(max_length=200)

    # It contains timestamp (the time at which notification was sent)
    created_date = models.DateTimeField(default=timezone.now)
