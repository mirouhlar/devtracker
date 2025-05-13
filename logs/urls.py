from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.log_create, name='log_create'),
    path('<int:pk>/edit/', views.log_edit, name='log_edit'),
    path('<int:pk>/delete/', views.log_delete, name='log_delete'),
]
