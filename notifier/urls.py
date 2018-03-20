__author__ = "Vivek Raj, Kapil Goyal and Rohit Pant"
__credits__ = ["Nitin Kedia", "Jatin Goyal", "Sahib Khan",
                    "Sparsh Bansal"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Vivek Raj"
__email__ = "raj.vivek.151297@gmail.com"
__status__ = "Development"

# import other libraries
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from django.views.generic import RedirectView

# here url formats are defined which will be encountered.
urlpatterns = [
    # url to login will be of format 127.0.0.1:8000/login/
    url(r'^login/$', views.login_custom, name='login_custom'),

    # url to home will be of format 127.0.0.1:8000/
    url(r'^$', RedirectView.as_view(url='/notification_list/', permanent=True),name='home'),

    # url to notification list will be of format 127.0.0.1:8000/notification/
    url(r'^notification/$', views.NotificationListView.as_view(), name='notification_list'),

    # url to notification list 2 will be of format 127.0.0.1:8000/notification_list/
    url(r'^notification_list/$', views.NotificationListView.as_view(), name='notification_list2'),

    # url to register a student will be of format 127.0.0.1:8000/student/create/
    url(r'^student/create/$', views.StudentCreate.as_view(), name='student_create'),

    # url to update student details will be of format 127.0.0.1:8000/student/update/<user uuid>
    url(r'^student/update/(?P<pk>\d+)/$', login_required(views.StudentUpdate.as_view()), name='student_update'),

    # url to state change will be of format 127.0.0.1:8000/state/<user uuid>
    url(r'^state/(?P<pk>\d+)$', views.stateAnalyser, name='state'),

    # url to response of notification will be of format 127.0.0.1:8000/notification/delete/<user uuid>/
    url(r'^notification/delete/(?P<pk>\d+)/$', login_required(views.NotificationDelete.as_view()), name='notification_delete'),
]
