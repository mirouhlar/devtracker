from django.db import models
from django.conf import settings

class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contributed_projects', blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
