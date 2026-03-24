from django.contrib import admin
from .models import Resident, Complaint, Announcement, Maintenance, Payment, Guard, Visitor


class ResidentAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'block', 'flat_number')


admin.site.register(Resident, ResidentAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'resident', 'status', 'created_at')

admin.site.register(Complaint, ComplaintAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

admin.site.register(Announcement, AnnouncementAdmin)


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'due_date', 'created_at')

admin.site.register(Maintenance, MaintenanceAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'maintenance', 'status', 'created_at')

admin.site.register(Payment,PaymentAdmin)



class GuardAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone')

admin.site.register(Guard, GuardAdmin)


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name', 'resident', 'status', 'entry_time')

admin.site.register(Visitor, VisitorAdmin)