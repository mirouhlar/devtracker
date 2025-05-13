from django.shortcuts import render
from projects.models import Project

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:10]
    return render(request, 'home.html', {'projects': projects})
