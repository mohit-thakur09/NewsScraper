from django import forms
from django.forms import fields, widgets
from .models import UserFeedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm

class Feedback(forms.ModelForm):
    class Meta:
        model=UserFeedback
        fields=['name','email','feedback']
        labels={'email':'Enter Email','feedback':'Write feedback','name':'Enter name'}
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'feedback':forms.Textarea(attrs={'class':'form-control'})}
    
class SignupForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    class Meta:
        model=User
        fields=['username']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
    
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Username')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    class Meta:
        model=User
        fields=['username','password']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class ChangePasswordForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
