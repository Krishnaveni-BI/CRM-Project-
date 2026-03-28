from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin / Team Lead (Vikas)'),
        ('team1', 'Team 1 – Caller'),
        ('team2', 'Team 2 – Follow-up Agent'),
        ('manager', 'Manager / Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='team1')
    phone = models.CharField(max_length=15, blank=True)

    def is_admin_lead(self):
        return self.role == 'admin'

    def is_team1(self):
        return self.role == 'team1'

    def is_team2(self):
        return self.role == 'team2'

    def is_manager(self):
        return self.role == 'manager'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
