from django.contrib import admin
from .models import Farmer, Team1Assignment, Team2Assignment, FarmerUploadLog


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('farmer_id', 'name', 'phone', 'village', 'district', 'crop')
    search_fields = ('farmer_id', 'name', 'phone', 'village', 'district')
    list_filter = ('district', 'crop', 'state')


@admin.register(Team1Assignment)
class Team1AssignmentAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'assigned_to', 'call_status', 'interest_status', 'assigned_at')
    list_filter = ('call_status', 'interest_status', 'assigned_to')
    search_fields = ('farmer__name', 'farmer__phone', 'assigned_to__username')


@admin.register(Team2Assignment)
class Team2AssignmentAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'assigned_to', 'followup_status', 'final_response', 'assigned_at')
    list_filter = ('followup_status', 'final_response', 'assigned_to')
    search_fields = ('farmer__name', 'farmer__phone', 'assigned_to__username')


@admin.register(FarmerUploadLog)
class FarmerUploadLogAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded_by', 'total_records', 'success_records', 'failed_records', 'uploaded_at')
    list_filter = ('uploaded_by',)
