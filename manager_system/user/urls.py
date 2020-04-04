from django.conf.urls import url
from user.views import *

urlpatterns=[
    url(r'^login/$',login),
    url(r'^regist/$',regist),
    url(r'^regist_handle/$',regist_handle),
    url(r'^login_handle/$',login_handle),
    url(r'^vfcode/$',vfcode),
]