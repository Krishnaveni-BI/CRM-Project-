from django import forms
from django.contrib.auth import get_user_model
from .models import Farmer, Team1Assignment, Team2Assignment

User = get_user_model()


class FarmerUploadForm(forms.Form):
    file = forms.FileField(
        label='Select CSV or Excel file',
        widget=forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv,.xlsx,.xls'})
    )


class BulkAssignTeam1Form(forms.Form):
    """Admin assigns selected farmers to a Team 1 member."""
    farmer_ids = forms.CharField(widget=forms.HiddenInput())
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.filter(role='team1'),
        empty_label='-- Select Team 1 Member --',
        widget=forms.Select(attrs={'class': 'form-select form-select-lg'})
    )


class BulkAssignTeam2Form(forms.Form):
    """Admin assigns interested farmers to a Team 2 member."""
    farmer_ids = forms.CharField(widget=forms.HiddenInput())
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.filter(role='team2'),
        empty_label='-- Select Team 2 Member --',
        widget=forms.Select(attrs={'class': 'form-select form-select-lg'})
    )


class Team1UpdateForm(forms.ModelForm):
    """Team 1 caller updates call & interest status."""
    class Meta:
        model = Team1Assignment
        fields = ['call_status', 'interest_status', 'call_remarks', 'called_at']
        widgets = {
            'call_status': forms.Select(attrs={'class': 'form-select'}),
            'interest_status': forms.Select(attrs={'class': 'form-select'}),
            'call_remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add any notes...'}),
            'called_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class Team2UpdateForm(forms.ModelForm):
    """Team 2 agent updates follow-up & final response."""
    class Meta:
        model = Team2Assignment
        fields = ['followup_status', 'final_response', 'followup_remarks', 'contacted_at']
        widgets = {
            'followup_status': forms.Select(attrs={'class': 'form-select'}),
            'final_response': forms.Select(attrs={'class': 'form-select'}),
            'followup_remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add follow-up notes...'}),
            'contacted_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class FarmerFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by name, village, phone...'})
    )
    call_status = forms.ChoiceField(
        required=False,
        choices=[('', 'All Call Status')] + Team1Assignment.CALL_STATUS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    interest_status = forms.ChoiceField(
        required=False,
        choices=[('', 'All Interest Status')] + Team1Assignment.INTEREST_STATUS,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
