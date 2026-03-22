from django.db import models
from django.contrib.auth.models import User


class Resident(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    block = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Resolved', 'Resolved')
        ],
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Announcement(models.Model):

    title = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    




class Maintenance(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Paid', 'Paid')],
        default='Pending'
    )
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.maintenance} - {self.status}"