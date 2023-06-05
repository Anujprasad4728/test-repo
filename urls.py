
#dublicate file created through copy
from django.urls import path

# Create your views here.
from . import views

urlpatterns=[
    path('', views.myview)
    ]
