from django.contrib import admin
from .models import UserFeedback

# Register your models here.

class UserFeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','feedback')

admin.site.register(UserFeedback,UserFeedbackAdmin)  

