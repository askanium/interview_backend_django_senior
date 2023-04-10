from django.contrib import admin

from interview.profiles.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
