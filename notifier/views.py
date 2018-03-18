

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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('student_create')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    return render(request,'index.html')

class StudentDetailView(generic.DetailView):
    model=Student

class StudentCreate(CreateView):
    model = Student
    form_class=StudentForm
    
class StudentUpdate(UpdateView):
    model = Student
    fields = ['user','department','mail','phone']

def login_custom(request):
    if(request.POST):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        return redirect('home')
    return render(request, 'registration/login.html')

class NotificationListView(generic.ListView):
    model = Notification

from django.contrib.auth.models import User

def state(request,pk):
    state = request.GET.get('state')
    if int(state)<4:
        user = User.objects.get(id=pk)
        noti = Notification.objects.create(user=user.student,text="Please pay attention")
        print("Notification to "+user.username+" has been send")
        return render(request, 'notification_sent.html')
    else:
        user = User.objects.get(id=pk)
        print(user.username+" is paying attention")
        return render(request, 'notification_not_sent.html')

class NotificationDelete(DeleteView):
    model = Notification
    def get_success_url(self):
        return reverse_lazy( 'notification_list')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)