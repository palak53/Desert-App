from django.shortcuts import render
from .models import Notification

def notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notifications.html', {'notifications': notifications})
