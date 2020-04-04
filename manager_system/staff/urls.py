from django.conf.urls import url
from staff.views import *

urlpatterns=[
    url(r'^home/$',home),
    url(r'^detail_(\d+)/$',detail),
    url(r'^delete_(\d+)/$',delete,name='del'),
    url(r'^add/$',add),
    url(r'^add_handle/$',add_handle,name='ahandle'),
    url(r'^edt/$',edt,name='edt'),
    url(r'^edt_handle/$',edt_handle,name='ehandle'),
]