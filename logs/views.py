from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DevLog
from .forms import DevLogForm

@login_required
def log_create(request):
    if request.method == 'POST':
        form = DevLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.author = request.user
            log.save()
            return redirect('dashboard')
    else:
        form = DevLogForm()
        form.fields['project'].queryset = request.user.projects.all() | request.user.contributed_projects.all()
    return render(request, 'logs/log_form.html', {'form': form})

@login_required
def log_edit(request, pk):
    log = get_object_or_404(DevLog, pk=pk, author=request.user)
    if request.method == 'POST':
        form = DevLogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DevLogForm(instance=log)
        form.fields['project'].queryset = request.user.projects.all()
    return render(request, 'logs/log_form.html', {'form': form})

@login_required
def log_delete(request, pk):
    log = get_object_or_404(DevLog, pk=pk, author=request.user)
    if request.method == 'POST':
        log.delete()
        return redirect('dashboard')
    return render(request, 'logs/log_confirm_delete.html', {'log': log})
