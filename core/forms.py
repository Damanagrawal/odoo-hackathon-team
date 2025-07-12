from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserSkill, SwapRequest, Feedback

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

class UserSkillForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        fields = ['skill', 'skill_type']
        widgets = {
            'skill': forms.Select(attrs={'class': 'form-control'}),
            'skill_type': forms.Select(attrs={'class': 'form-control'}),
        }

class SwapRequestForm(forms.ModelForm):
    class Meta:
        model = SwapRequest
        fields = ['to_user', 'skill_offered', 'skill_requested']
        widgets = {
            'to_user': forms.Select(attrs={'class': 'form-control'}),
            'skill_offered': forms.Select(attrs={'class': 'form-control'}),
            'skill_requested': forms.Select(attrs={'class': 'form-control'}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['swap', 'rating', 'comment']
        widgets = {
            'swap': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Share your experience...'}),
        }