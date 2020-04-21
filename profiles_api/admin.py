from django.contrib import admin
from profiles_api import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff')


admin.site.register(models.UserProfile, UserProfileAdmin)
