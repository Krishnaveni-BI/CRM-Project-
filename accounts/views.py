from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import LoginForm, UserCreateForm

User = get_user_model()


# ─────────────────────────────────────────────
#  MAIN LOGIN (Admin / Manager)
# ─────────────────────────────────────────────

def login_view(request):
    """Main login page — for Admin (Vikas) and Manager only."""
    if request.user.is_authenticated:
        return redirect('dashboard_redirect')
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.get_full_name() or user.username}!")
            return redirect('dashboard_redirect')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')


@login_required
def dashboard_redirect(request):
    role = request.user.role
    if role == 'admin':
        return redirect('assign_team1')
    elif role == 'team1':
        return redirect('team1_dashboard')
    elif role == 'team2':
        return redirect('team2_dashboard')
    elif role == 'manager':
        return redirect('manager_dashboard')
    return redirect('login')


# ─────────────────────────────────────────────
#  TEAM 1 QUICK LOGIN
# ─────────────────────────────────────────────

def team1_quick_login(request):
    """Team 1 separate login page with username + password."""
    if request.user.is_authenticated:
        return redirect('team1_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'team1' and user.is_active:
            login(request, user)
            messages.success(request, f"Welcome {user.get_full_name() or user.username}!")
            return redirect('team1_dashboard')
        else:
            messages.error(request, "Invalid username or password. Make sure you are a Team 1 member.")
    return render(request, 'accounts/team1_login.html')


# ─────────────────────────────────────────────
#  TEAM 2 QUICK LOGIN
# ─────────────────────────────────────────────

def team2_quick_login(request):
    """Team 2 separate login page with username + password."""
    if request.user.is_authenticated:
        return redirect('team2_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'team2' and user.is_active:
            login(request, user)
            messages.success(request, f"Welcome {user.get_full_name() or user.username}!")
            return redirect('team2_dashboard')
        else:
            messages.error(request, "Invalid username or password. Make sure you are a Team 2 member.")
    return render(request, 'accounts/team2_login.html')


# ─────────────────────────────────────────────
#  USER MANAGEMENT (Admin only)
# ─────────────────────────────────────────────

@login_required
def user_list(request):
    if request.user.role != 'admin':
        messages.error(request, "Access denied.")
        return redirect('dashboard_redirect')
    users = User.objects.all().order_by('role', 'first_name')
    return render(request, 'accounts/user_list.html', {'users': users})


@login_required
def user_delete(request, pk):
    if request.user.role != 'admin':
        messages.error(request, "Access denied.")
        return redirect('dashboard_redirect')
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        if user.username == request.user.username:
            messages.error(request, "You cannot delete yourself.")
        else:
            name = user.get_full_name() or user.username
            user.delete()
            messages.success(request, f"User '{name}' deleted successfully.")
    return redirect('user_list')


@login_required
def user_create(request):
    if request.user.role != 'admin':
        messages.error(request, "Access denied.")
        return redirect('dashboard_redirect')
    form = UserCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        messages.success(request, f"User '{user.username}' created successfully.")
        return redirect('user_list')
    return render(request, 'accounts/user_form.html', {'form': form, 'title': 'Create New User'})
