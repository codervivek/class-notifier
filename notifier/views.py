__author__ = "Vivek Raj, Kapil Goyal and Rohit Pant"
__credits__ = ["Nitin Kedia", "Jatin Goyal", "Sahib Khan",
                    "Sparsh Bansal"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Vivek Raj"
__email__ = "raj.vivek.151297@gmail.com"
__status__ = "Development"


# import other libraries
from django.shortcuts import render
from classnotifier.forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Max
from django.views import generic
from django.contrib.auth.models import User
from .models import Student, Notification
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

# view to make new user
def signup(request):
    # if there is signup details
    if request.method == 'POST':
        # get signup form
        form = SignUpForm(request.POST)
        if form.is_valid():
            # retreive form details
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # authenticate and login user
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('student_create')
    else:
        # respond with a empty form
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# view to homepage
@login_required(login_url='/login/')
def home(request):
    return render(request,'index.html')

# detail view for every student
class StudentDetailView(generic.DetailView):
    model=Student

# view to create a new student object
class StudentCreate(CreateView):
    model = Student
    form_class=StudentForm

# view to create a update student object 
class StudentUpdate(UpdateView):
    model = Student
    fields = ['user','department','mail','phone']

# view to check if login details are correct
def login_custom(request):
    if(request.POST):
        # get username and password
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the user so that he does not have login after register
        user = authenticate(request, username=username, password=password)
        return redirect('home')
    return render(request, 'registration/login.html')

# view for showing notification list to a student
class NotificationListView(generic.ListView):
    model = Notification

from django.contrib.auth.models import User

# view to anaylse state coming from parent system
def stateAnalyser(request,pk):
    # pk is id of user whose state has to be analysed

    # get state parameter
    state = request.GET.get('state')
    
    # if state is less than 4 then we have send notification
    if int(state)<4:
        
        # exception handling when state or id might be incorrect
        try:
            # get student user with given id
            user = User.objects.get(id=pk)

            # create new notification object
            noti = Notification.objects.create(user=user.student,text="Please pay attention")

            # print if notification is send
            print("Notification to "+user.username+" has been send")
            
            # return notification send confirmation page
            return render(request, 'notification_sent.html')
        
        # if some error occured
        except Exception as e:

            # return notification not send page
            return render(request, 'notification_not_sent.html')
            
    else:

        # get student user with given id and display he/she is paying attention
        user = User.objects.get(id=pk)
        print(user.username+" is paying attention")

        # return notification not send page
        return render(request, 'notification_not_sent.html')

# view when a student responds to a message
class NotificationDelete(DeleteView):
    model = Notification

    # redirect url when the notification is dismissed
    def get_success_url(self):
        return reverse_lazy( 'notification_list')

    # get request or post request both will delete the message
    # get and post are inherited from parent class
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)