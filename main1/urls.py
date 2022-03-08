from django.contrib import admin
from django.urls import path
from main1 import views

urlpatterns = [
    path("", views.index, name='main1'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("loginform.html", views.loginform, name='loginform'),
    path("signout", views.signout, name='signout'),
    path("product", views.products, name='product'),
]
