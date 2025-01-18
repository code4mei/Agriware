from django.urls import path
from ecommerceapp import views

urlpatterns =[
    path('',views.index1,name="index1"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('prediction',views.prediction,name="prediction"),
]