from django.shortcuts import render, redirect
from .models import Resident, Complaint, Announcement, Maintenance
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# ---------------- LOGIN ----------------
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):

    resident = Resident.objects.get(user=request.user)

    resident_count = Resident.objects.count()
    complaint_count = Complaint.objects.count()
    recent_complaints = Complaint.objects.filter(resident=resident).order_by('-created_at')[:5]
    maintenances = Maintenance.objects.all().order_by('-created_at')
    announcements = Announcement.objects.all().order_by('-created_at')[:5]
    announcements_count = Announcement.objects.count()

    context = {
        "maintenances": maintenances,
        "resident_count": resident_count,
        "complaint_count": complaint_count,
        "recent_complaints": recent_complaints,
        "announcements": announcements,
        "annoucements_count": announcements_count
    }

    return render(request, "dashboard.html", context)


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("login")


# ---------------- HOME ----------------
def home(request):
    return render(request, "home.html")


# ---------------- VIEW COMPLAINTS ----------------
@login_required
def complaints(request):

    resident = Resident.objects.get(user=request.user)

    complaints = Complaint.objects.filter(resident=resident)

    return render(request, "complaints.html", {"complaints": complaints})


# ---------------- ADD COMPLAINT ----------------
@login_required
def add_complaint(request):

    resident = Resident.objects.get(user=request.user)

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")

        Complaint.objects.create(
            resident=resident,
            title=title,
            description=description
        )

        return redirect("complaints")

    return render(request, "complaints/add_complaint.html")