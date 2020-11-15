from django.conf import settings
# exceptions / validators
from django.core.exceptions import ValidationError

from django.db import models

from django.utils import timezone


# Create your models here.

"""class UserDayTime(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    today = models.DateField(default=timezone.now)
"""""

class UserActivityManager(models.Manager):
    def current(self, user=None):
        if user is None:
            return None
        current_obj = self.get_queryset().filter(user=user).order_by('-timestamp').first()
        return current_obj

    def toggle(self, user):
        if user is None:
            return None
        last_item = self.current(user)
        if last_item is not None:
            if last_item.activity == "checkin":
                activity = "checkout"
        obj = self.model(
                user=user,
                activity=activity
        )
        obj.save()
        return obj

USER_ACTIVITY_CHOICES = (
    ('checkin', 'Check In'),
    ('checkout', 'Check Out'),
)


class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.CharField(max_length=120, default='checkin', choices=USER_ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserActivityManager()

    class Meta:
        verbose_name = "User Activity"
        verbose_name_plural = "User Activities"

    def __unicode__(self):
        return str(self.activity)

    def __str__(self):
        return self.activity

# Validation for activities

    def clean(self, *args, **kwargs):
        if self.user:
            user_activities = UserActivity.objects.exclude(
                                    id=self.id
                                    ).filter(
                                        user=self.user
                                    ).order_by('-timestamp')
            if user_activities.exists():
                recent_ = user_activities.first()
                if self.activity == recent_.activity:
                    message = "%s is not a valid activity for this user" %(self.get_activity_display())
                    raise ValidationError(message)
            else:
                if self.activity != 'checkin':
                    message = "%s is not a valid activity for this user as a first activity" % (self.get_activity_display())
                    raise ValidationError(message)

        return super(UserActivity, self).clean(*args, **kwargs)



