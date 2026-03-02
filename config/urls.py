from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin
    path('accounts/', include('accounts.urls')),  # Your app URLs
]