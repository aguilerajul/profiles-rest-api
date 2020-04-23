from django.contrib import admin
from .models import UserProfile, ProfileFeedItem


class UserProfileAdmin(admin.ModelAdmin):
    """Custom Fields for User Profile"""
    list_display = ('email', 'name', 'is_active', 'is_staff')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem)
