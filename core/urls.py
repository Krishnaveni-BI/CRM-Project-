from django.urls import path
from . import views

urlpatterns = [
    # Admin
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/redirect/', views.dashboard_redirect_core, name='dashboard_redirect'),
    path('farmers/upload/', views.upload_farmers, name='upload_farmers'),

    # Team 1 Assignment & Unassignment
    path('farmers/assign/team1/', views.assign_team1, name='assign_team1'),
    path('farmers/unassign/team1/<int:pk>/', views.unassign_team1, name='unassign_team1'),
    path('users/create/team1/', views.user_create_team1, name='user_create_team1'),

    # Team 2 Assignment & Unassignment
    path('farmers/assign/team2/', views.assign_team2, name='assign_team2'),
    path('farmers/unassign/team2/<int:pk>/', views.unassign_team2, name='unassign_team2'),
    path('users/create/team2/', views.user_create_team2, name='user_create_team2'),

    # Farmer Views
    path('farmers/all/', views.all_farmers_view, name='all_farmers'),
    path('farmers/interested/', views.interested_farmers_view, name='interested_farmers'),
    path('farmers/confirmed/', views.confirmed_farmers_view, name='confirmed_farmers'),
    path('farmers/export/', views.export_farmers_csv, name='export_csv'),
    path('farmers/ready-to-work/', views.ready_to_work_view, name='ready_to_work'),

    # Team 1
    path('dashboard/team1/', views.team1_dashboard, name='team1_dashboard'),
    path('team1/update/<int:pk>/', views.team1_update, name='team1_update'),
    path('team1/quick-update/<int:pk>/', views.team1_quick_update, name='team1_quick_update'),

    # Team 2
    path('dashboard/team2/', views.team2_dashboard, name='team2_dashboard'),
    path('team2/update/<int:pk>/', views.team2_update, name='team2_update'),
    path('team2/quick-reached/<int:pk>/', views.team2_quick_reached, name='team2_quick_reached'),
    path('team2/quick-decision/<int:pk>/', views.team2_quick_decision, name='team2_quick_decision'),

    # Manager
    path('dashboard/manager/', views.manager_dashboard, name='manager_dashboard'),
]
