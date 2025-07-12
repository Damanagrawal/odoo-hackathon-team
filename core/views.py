from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserSkillForm, SwapRequestForm, FeedbackForm
from .models import Skill, UserSkill, SwapRequest, Feedback
from django.contrib.auth.models import User


def index(request):
    return render(request, 'core/index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def profile(request):
    skills = UserSkill.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UserSkillForm(request.POST)
        if form.is_valid():
            user_skill = form.save(commit=False)
            user_skill.user = request.user
            user_skill.save()
            return redirect('profile')
    else:
        form = UserSkillForm()
    return render(request, 'core/profile.html', {'skills': skills, 'form': form})


@login_required
def browse_users(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'core/browse.html', {'users': users})


@login_required
def request_swap(request):
    if request.method == 'POST':
        form = SwapRequestForm(request.POST)
        if form.is_valid():
            swap = form.save(commit=False)
            swap.from_user = request.user
            swap.save()
            return redirect('index')
    else:
        form = SwapRequestForm()
    return render(request, 'core/request_swap.html', {'form': form})


@login_required
def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.from_user = request.user
            feedback.save()
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'core/feedback.html', {'form': form})