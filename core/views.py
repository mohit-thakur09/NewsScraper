from django.shortcuts import render,HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
from django.utils import timezone
from .forms import Feedback,SignupForm,LoginForm,ChangePasswordForm
from .models import UserFeedback
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/login/')
def yourstory(request):
    l = []
    url = 'https://yourstory.com/feed'
    content = requests.get(url).content
    soup = BeautifulSoup(content, "html.parser")
    for n, t in enumerate(soup.findAll("title")):
        l.append(str(n) + " - " + t.text)
    l.pop(0)
    todays_date = datetime.datetime.now()
    return render(request,'core/yourstory.html',{'links':l,'date':todays_date})

@login_required(login_url='/login/')
def hackernews(request):
    url='https://news.ycombinator.com/'
    l=[]
    content = urlopen(url).read()
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        l.append(str(i+1)+' - '+tag.text + '\n') if tag.text!='More' else ''
    todays_date = datetime.datetime.now()
    return render(request,'core/hackernews.html',{'links':l,'date':todays_date})
       

def home(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html')
    else:
        return HttpResponseRedirect('/login/')


@login_required(login_url='/login/')
def about(request):
    if request.method=="POST":
        feedback_obj=Feedback(request.POST)
        if feedback_obj.is_valid():
            name_val=feedback_obj.cleaned_data['name']
            email_val=feedback_obj.cleaned_data['email']
            feedback_val=feedback_obj.cleaned_data['feedback']
            UserFeedback_obj=UserFeedback(email=email_val,feedback=feedback_val,name=name_val,date=timezone.now())
            UserFeedback_obj.save()
            messages.success(request,'Feedback submitted !!')
            feedback_obj=Feedback()
            
    else:
        feedback_obj=Feedback()
    latest_feedback_list = UserFeedback.objects.order_by("-date")[:5]
    return render(request,'core/about.html',{
        'form':feedback_obj,
        'latest_feedback':latest_feedback_list
    })

def landing(request):
    return render(request,'core/landing.html')

def Usersignup(request):
    if request.method=="POST":
        signup_obj=SignupForm(request.POST)
        if signup_obj.is_valid():
            signup_obj.save()
            messages.success(request,'Signed up successfully !!')
            return HttpResponseRedirect('/login/')
    else:
        signup_obj=SignupForm()
    return render(request,'core/signup.html',{'form':signup_obj})


def Userlogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            login_obj=LoginForm(request=request,data=request.POST)
            if login_obj.is_valid():
                username_val=login_obj.cleaned_data['username']
                pass_val=login_obj.cleaned_data['password']
                user = authenticate(username=username_val,password=pass_val)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully !!')
                    return HttpResponseRedirect('/home/')
        else:
            login_obj=LoginForm()
        return render(request,'core/login.html',{'form':login_obj})
    else:
        return HttpResponseRedirect('/home/')


def Userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def Userchangepassword(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            changepass_obj=ChangePasswordForm(user=request.user,data=request.POST)
            if changepass_obj.is_valid():
                changepass_obj.save()
                update_session_auth_hash(request,changepass_obj.user)
                messages.success(request,'Password changed successfully !!')
                return HttpResponseRedirect('/home/')
        else:
            changepass_obj=ChangePasswordForm(user=request.user)
        return render(request,'core/changepassword.html',{'form':changepass_obj})
    else:
        return HttpResponseRedirect('/login/')