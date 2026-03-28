"""
Run this once to create sample users and 20 demo farmers.
Command: python seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farmer_crm.settings')
django.setup()

from django.contrib.auth import get_user_model
from core.models import Farmer

User = get_user_model()

print("Creating users...")

# Admin
vikas, _ = User.objects.get_or_create(username='vikas', defaults={
    'first_name': 'Vikas', 'last_name': 'Sharma',
    'email': 'vikas@example.com', 'role': 'admin', 'is_staff': True
})
vikas.set_password('admin123')
vikas.save()

# Team 1 callers
team1_data = [
    ('krisy',   'Krisy',   'Patel',   'krisy@example.com'),
    ('arjun',   'Arjun',   'Singh',   'arjun@example.com'),
    ('priya',   'Priya',   'Mehta',   'priya@example.com'),
]
team1_users = []
for uname, fname, lname, email in team1_data:
    u, _ = User.objects.get_or_create(username=uname, defaults={
        'first_name': fname, 'last_name': lname,
        'email': email, 'role': 'team1'
    })
    u.set_password('team1pass')
    u.save()
    team1_users.append(u)

# Team 2 follow-up agents
team2_data = [
    ('rekha',   'Rekha',   'Verma',   'rekha@example.com'),
    ('suresh',  'Suresh',  'Nair',    'suresh@example.com'),
]
team2_users = []
for uname, fname, lname, email in team2_data:
    u, _ = User.objects.get_or_create(username=uname, defaults={
        'first_name': fname, 'last_name': lname,
        'email': email, 'role': 'team2'
    })
    u.set_password('team2pass')
    u.save()
    team2_users.append(u)

# Manager
mgr, _ = User.objects.get_or_create(username='manager', defaults={
    'first_name': 'Rajesh', 'last_name': 'Kumar',
    'email': 'manager@example.com', 'role': 'manager'
})
mgr.set_password('mgr123')
mgr.save()

print("  ✅ Users created.")

# Sample farmers
print("Creating 20 sample farmers...")
farmers_data = [
    ('F001','Ramesh Kumar',     '9876543201','Nashik',     'Nashik',    'Maharashtra','Grapes',  2.5),
    ('F002','Sunita Devi',      '9876543202','Pune',       'Pune',      'Maharashtra','Onion',   1.8),
    ('F003','Govind Patil',     '9876543203','Solapur',    'Solapur',   'Maharashtra','Soybean', 3.2),
    ('F004','Meena Kumari',     '9876543204','Nagpur',     'Nagpur',    'Maharashtra','Orange',  2.0),
    ('F005','Raju Yadav',       '9876543205','Aurangabad', 'Aurangabad','Maharashtra','Cotton',  4.0),
    ('F006','Laxmi Bai',        '9876543206','Satara',     'Satara',    'Maharashtra','Sugarcane',5.0),
    ('F007','Shankar Reddy',    '9876543207','Bijapur',    'Bijapur',   'Karnataka',  'Jowar',   2.2),
    ('F008','Kavitha Rao',      '9876543208','Hubli',      'Dharwad',   'Karnataka',  'Wheat',   1.5),
    ('F009','Manjunath Gowda',  '9876543209','Mysore',     'Mysore',    'Karnataka',  'Ragi',    1.0),
    ('F010','Parvathi Naidu',   '9876543210','Guntur',     'Guntur',    'Andhra Pradesh','Chilli',3.0),
    ('F011','Venkat Raman',     '9876543211','Tirupati',   'Chittoor',  'Andhra Pradesh','Tomato',1.2),
    ('F012','Anitha Lakshmi',   '9876543212','Warangal',   'Warangal',  'Telangana',  'Maize',   2.8),
    ('F013','Balu Naik',        '9876543213','Nanded',     'Nanded',    'Maharashtra','Tur Dal',  1.6),
    ('F014','Shanta Bai',       '9876543214','Kolhapur',   'Kolhapur',  'Maharashtra','Rice',    3.5),
    ('F015','Deepak Jadhav',    '9876543215','Sangli',     'Sangli',    'Maharashtra','Grapes',  2.0),
    ('F016','Kamala Devi',      '9876543216','Amravati',   'Amravati',  'Maharashtra','Cotton',  4.5),
    ('F017','Ramakant Shinde',  '9876543217','Jalgaon',    'Jalgaon',   'Maharashtra','Banana',  1.8),
    ('F018','Seema Patil',      '9876543218','Dhule',      'Dhule',     'Maharashtra','Onion',   2.1),
    ('F019','Kiran Kulkarni',   '9876543219','Nashik',     'Nashik',    'Maharashtra','Pomegranate',2.4),
    ('F020','Tanaji More',      '9876543220','Raigad',     'Raigad',    'Maharashtra','Mango',   3.0),
]

for row in farmers_data:
    Farmer.objects.get_or_create(
        farmer_id=row[0],
        defaults={
            'name': row[1], 'phone': row[2],
            'village': row[3], 'district': row[4],
            'state': row[5], 'crop': row[6], 'land_acres': row[7]
        }
    )

print(f"  ✅ {Farmer.objects.count()} farmers in database.")

print("\n✅ DONE! All sample data created.")
print("\n── LOGIN CREDENTIALS ──────────────────────")
print("  Admin (Vikas)  : username=vikas       password=admin123")
print("  Team 1 Caller  : username=krisy       password=team1pass")
print("  Team 1 Caller  : username=arjun       password=team1pass")
print("  Team 2 Agent   : username=rekha       password=team2pass")
print("  Manager        : username=manager     password=mgr123")
print("───────────────────────────────────────────")
print("Run: python manage.py runserver")
print("Open: http://127.0.0.1:8000/")
