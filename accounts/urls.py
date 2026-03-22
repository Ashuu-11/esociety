from django.urls import path
from .views import login_view, logout_view, complaints, add_complaint

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/",logout_view,name="logout"),
    path("complaints/", complaints, name="complaints"),
    path("add-complaint/", add_complaint, name="add_complaint"),
]