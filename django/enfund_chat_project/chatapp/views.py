from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q


def home(request):
    users = User.objects.exclude(username=request.user.username)
    print("users: ", users)
    return render(request, "home.html", {"users": users})

def chat(request, user_id):
    users = User.objects.exclude(username = request.user.username)
    other_user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    ).order_by('created_on')
    print("users: ", users)
    return render(request, "chat.html", {"users": users, "other_user": other_user, "messages": messages})