from django.shortcuts import render, redirect
from .models import User

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            User.objects.create(username=username, password=password)
            return redirect("signup")
        else:
            return render(request, "signup.html", {"error": "Passwords do not match"})

    return render(request, "signup.html")