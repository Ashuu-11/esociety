from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard, home, complaints, add_complaint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('', include('accounts.urls')),
    path('dashboard/', dashboard, name="dashboard"),
    path("complaints/", complaints, name="complaints"),
    path("add-complaint/", add_complaint, name="add_complaint"),
]