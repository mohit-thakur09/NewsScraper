from os import name
from django.urls import path
from . import views

app_name = "core"
urlpatterns=[
    path('',views.landing,name='landing'),
    path('home/', views.home, name='home'),
    path('yourstory', views.yourstory, name="yourstory"),
    path('hackernews',views.hackernews,name='hackernews'),
    path('about',views.about,name='about'),
    path('signup',views.Usersignup,name='signup'),
    path('login/',views.Userlogin,name='login'),
    path('logout',views.Userlogout,name='logout'),
    path('changepassword',views.Userchangepassword,name='changepassword'),

]