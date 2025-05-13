from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LogoutView

from projects.models import Project
from logs.models import DevLog
from goals.models import Goal
from .forms import CustomUserCreationForm, CustomUserEditForm

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@never_cache
@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user) | Project.objects.filter(contributors=request.user)
    projects = projects.distinct()
    logs = DevLog.objects.filter(author=request.user)
    goals = Goal.objects.filter(user=request.user)

    context = {
        'projects': projects,
        'logs': logs,
        'goals': goals,
        'goal_total': goals.count(),
        'goal_completed': goals.filter(is_completed=True).count(),
        'project_count': projects.count(),
        'log_count': logs.count(),
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user != project.owner and request.user not in project.contributors.all():
        return HttpResponseForbidden("You are not allowed to delete this project.")
    project.delete()
    return redirect('dashboard')

@login_required
def view_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'accounts/view_profile.html', {'profile_user': user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_profile', username=user.username)
    else:
        form = CustomUserEditForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': form})
