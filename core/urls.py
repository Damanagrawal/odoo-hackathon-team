from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('browse/', views.browse_users, name='browse'),
    path('request/', views.request_swap, name='request_swap'),
    path('feedback/', views.submit_feedback, name='feedback'),
]
