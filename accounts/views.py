from django.shortcuts import render, redirect
from .models import Resident, Complaint, Announcement, Maintenance, Guard, Visitor
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# ---------------- Resident LOGIN ----------------
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
    visitors = Visitor.objects.filter(resident=resident).order_by('-entry_time')

    context = {
        "maintenances": maintenances,
        "resident_count": resident_count,
        "complaint_count": complaint_count,
        "recent_complaints": recent_complaints,
        "announcements": announcements,
        "annoucements_count": announcements_count,
        "visitors": visitors
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




def guard_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            # Check if this user is a guard
            if Guard.objects.filter(user=user).exists():
                login(request, user)
                return redirect("guard_dashboard")

        return render(request, "guard/login.html", {"error": "Invalid credentials"})

    return render(request, "guard/login.html")


@login_required
def guard_dashboard(request):

    if not Guard.objects.filter(user=request.user).exists():
        return redirect("login")

    visitors = Visitor.objects.all().order_by('-entry_time')

    context = {
        "visitors": visitors,
        "visitors_count": Visitor.objects.count(),
    }

    return render(request, "guard/dashboard.html", context)



@login_required
def add_visitor(request):

    if not Guard.objects.filter(user=request.user).exists():
        return redirect("login")

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        resident_id = request.POST.get("resident")
        purpose = request.POST.get("purpose")

        resident = Resident.objects.get(id=resident_id)

        Visitor.objects.create(
            name=name,
            phone=phone,
            resident=resident,
            purpose=purpose
        )

        return redirect("guard_dashboard")

    residents = Resident.objects.all()

    return render(request, "guard/add_visitor.html", {"residents": residents})


@login_required
def approve_visitor(request, visitor_id):

    visitor = Visitor.objects.get(id=visitor_id)

    # security check
    if visitor.resident.user != request.user:
        return redirect("dashboard")

    visitor.status = "APPROVED"
    visitor.save()

    return redirect("dashboard")


@login_required
def reject_visitor(request, visitor_id):

    visitor = Visitor.objects.get(id=visitor_id)

    if visitor.resident.user != request.user:
        return redirect("dashboard")

    visitor.status = "REJECTED"
    visitor.save()

    return redirect("dashboard")