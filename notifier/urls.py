from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^login/$', views.login_custom, name='login_custom'),
    url(r'^$', RedirectView.as_view(url='/notification_list/', permanent=True),name='home'),
    url(r'^notification/$', views.NotificationListView.as_view(), name='notification_list'),
    url(r'^notification_list/$', views.NotificationListView.as_view(), name='notification_list2'),
    url(r'^student/create/$', views.StudentCreate.as_view(), name='student_create'),
    url(r'^student/update/(?P<pk>\d+)/$', login_required(views.StudentUpdate.as_view()), name='student_update'),
    url(r'^state/(?P<pk>\d+)$', views.state, name='state'),
    url(r'^notification/delete/(?P<pk>\d+)/$', login_required(views.NotificationDelete.as_view()), name='notification_delete'),
]