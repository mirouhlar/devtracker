from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.http import HttpResponseForbidden


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            form.save_m2m()
            messages.success(request, "Project created successfully!")
            project.contributors.add(request.user)
            return redirect('dashboard')
    else:
        form = ProjectForm(user=request.user)
    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)

    # Ensure the user is either the owner or a contributor
    if request.user != project.owner and request.user not in project.contributors.all():
        return HttpResponseForbidden("You are not allowed to edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project, user=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'projects/project_detail.html', {'project': project})
    else:
        form = ProjectForm(instance=project, user=request.user)
    return render(request, 'projects/project_form.html', {'form': form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.user != project.owner and request.user not in project.contributors.all():
        return HttpResponseForbidden("You are not allowed to delete this project.")

    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')  
    else:
        return render(request, 'projects/project_confirm_delete.html', {'project': project})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.user != project.owner and request.user not in project.contributors.all():
        return HttpResponseForbidden("You are not allowed to view this project.")

    return render(request, 'projects/project_detail.html', {'project': project})
