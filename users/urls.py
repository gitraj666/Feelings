__author__ = 'PRITHVIRAJ'

from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^logout/$',views.LogOutView.as_view(),name="logout"),
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^signup/$',views.SignUpView.as_view(),name="signup"),
    url(r'^dashboard/$',views.dashboard,name="dashboard"),
]

