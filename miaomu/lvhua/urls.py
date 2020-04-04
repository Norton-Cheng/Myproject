from django.conf.urls import url
from lvhua.views import *

urlpatterns=[
    url(r'index/$',index),
    url(r'about/$',about),
    url(r'message/$',message),
    url(r'messagehandle/$',messagehandle),
    url(r'product/$',product),
    url(r'productshow/$',productshow),
    url(r'productcate/$',productcate),
    url(r'jidi/$',jidi),
    url(r'honor/$',honor),
    url(r'news/$',news),
    url(r'newsshow/$',newsshow),
    url(r'contact/$',contact),
]