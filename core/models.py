from django.db import models
from django.conf import settings


class Farmer(models.Model):
    """Master farmer record loaded from CSV/Excel"""
    farmer_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    village = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    crop = models.CharField(max_length=100, blank=True)
    land_acres = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_id} – {self.name}"


class Team1Assignment(models.Model):
    """Admin assigns farmer to Team 1 caller"""
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE, related_name='team1_assignment')
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        limit_choices_to={'role': 'team1'}, related_name='team1_farmers'
    )
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        related_name='team1_assignments_made'
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    # Updated by Team 1 caller
    CALL_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('no_answer', 'No Answer'),
        ('busy', 'Busy / Call Back'),
    ]
    call_status = models.CharField(max_length=20, choices=CALL_STATUS, default='pending')

    INTEREST_STATUS = [
        ('not_called', 'Not Called Yet'),
        ('interested', 'Interested'),
        ('not_interested', 'Not Interested'),
        ('no_response', 'No Response'),
    ]
    interest_status = models.CharField(max_length=20, choices=INTEREST_STATUS, default='not_called')

    call_remarks = models.TextField(blank=True)
    called_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.farmer.name} → {self.assigned_to}"

    class Meta:
        ordering = ['-assigned_at']


class Team2Assignment(models.Model):
    """Admin assigns interested farmer to Team 2 follow-up agent"""
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE, related_name='team2_assignment')
    team1_assignment = models.OneToOneField(
        Team1Assignment, on_delete=models.CASCADE, related_name='team2_followup', null=True
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        limit_choices_to={'role': 'team2'}, related_name='team2_farmers'
    )
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        related_name='team2_assignments_made'
    )
    assigned_at = models.DateTimeField(auto_now_add=True)

    # Updated by Team 2 agent
    FOLLOWUP_STATUS = [
        ('pending', 'Pending Contact'),
        ('contacted', 'Contacted'),
        ('not_reachable', 'Not Reachable'),
    ]
    followup_status = models.CharField(max_length=20, choices=FOLLOWUP_STATUS, default='pending')

    FINAL_RESPONSE = [
        ('awaiting', 'Awaiting Response'),
        ('confirmed', 'Confirmed / Converted'),
        ('declined', 'Declined'),
        ('callback', 'Will Call Back'),
        ('no_response', 'No Response'),
    ]
    final_response = models.CharField(max_length=20, choices=FINAL_RESPONSE, default='awaiting')

    followup_remarks = models.TextField(blank=True)
    contacted_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.farmer.name} → {self.assigned_to} (Team 2)"

    class Meta:
        ordering = ['-assigned_at']


class FarmerUploadLog(models.Model):
    """Tracks CSV/Excel upload batches"""
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    file_name = models.CharField(max_length=200)
    total_records = models.IntegerField(default=0)
    success_records = models.IntegerField(default=0)
    failed_records = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Upload: {self.file_name} ({self.total_records} records)"
