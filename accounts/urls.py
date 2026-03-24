from django.urls import path
from .views import login_view, logout_view, complaints, add_complaint, guard_login, guard_dashboard,add_visitor,approve_visitor,reject_visitor

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/",logout_view,name="logout"),
    path("complaints/", complaints, name="complaints"),
    path("add-complaint/", add_complaint, name="add_complaint"),

    path("guard/login/", guard_login, name="guard_login"),
    path("guard/dashboard/", guard_dashboard, name="guard_dashboard"),
    path("guard/add-visitor/", add_visitor, name="add_visitor"),
    path("visitor/approve/<int:visitor_id>/", approve_visitor, name="approve_visitor"),
    path("visitor/reject/<int:visitor_id>/", reject_visitor, name="reject_visitor"),
]