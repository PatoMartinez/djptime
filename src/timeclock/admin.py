from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Register your models here.
from .models import UserActivity

class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'timestamp']

    list_filter = (
        'user',
        'activity',
        'timestamp',
    )
    ordering = (
        'user',
    )
    search_fields = ['user', 'activity']

    class Meta:
        model = UserActivity

admin.site.register(UserActivity,UserActivityAdmin)
