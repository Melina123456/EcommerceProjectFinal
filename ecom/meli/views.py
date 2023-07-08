from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def cart(request):
    return render(request, "cart.html")

def payment(request):
    return render(request, "payment.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # check input
        # TODO
        try:
            users = User.objects.create_user(username, email, password1)
            # users.first_name = fname
            # users.last_name = lname
            users.save()
        except Exception as e:
            print("username already taken")
            return render(request, "sign_up.html")

        return HttpResponse("User created successfully")

    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("loggedin")
            return redirect("/")

        else:
            print("cant login try again ")
            return HttpResponse("first first create a account")

    return render(request, "signin.html")


def signout(request):
    logout(request)
    return redirect("/cart")
