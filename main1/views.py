import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from main1.models import product
# Create your views here.


def index(request):
    return render(request, "index.html")


def loginform(request):
    return render(request, "loginform.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        uemail = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username):
            messages.success(request, "User name already exist")
            return render(request, "loginform.html")

        if User.objects.filter(email=uemail):
            messages.success(request, "Email already Registered")
            return render(request, "loginform.html")

        if len(username) > 15:
            messages.success(request, "user name must be under 15")
            return render(request, "loginform.html")

        ouruser = User.objects.create_user(username, uemail, password)
        ouruser.save()
        return render(request, "loginform.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "loginform.html")


def signout(request):
    logout(request)
    return render(request, "index.html")


def products(request):
     p=product.get_all_products()
     print(p)
     return render(request, "product.html", {'products':p})
