from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("landing:home")

    return render(request, "accounts/login.html")


def logout_view(request):

    logout(request)
    return redirect("landing:home")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(username=username, password=password)

        return redirect("accounts:login")

    return render(request, "accounts/register.html")


@login_required
def profile_view(request):

    return render(request, "accounts/profile.html")