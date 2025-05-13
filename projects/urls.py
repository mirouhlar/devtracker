from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
]
