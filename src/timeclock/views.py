from django.shortcuts import render
from django.views import View
from .models import UserActivity

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "timeclock/index.html", {})

# Login Required
class ActivityView(View):
    def get(self, request, *args, **kwargs):
        # current activity
        return render(request, "timeclock/activity-view.html", {})

    def post(self, request, *args, **kwargs):
        new_act = UserActivity.objects.create(user=request.user, activity='checkin')
        return render(request, "timeclock/activity-view.html", {})

