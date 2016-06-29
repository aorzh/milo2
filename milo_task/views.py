from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from datetime import date


def users_list(request):
    context_dict = {}
    profiles = Profile.objects.all()

    context_dict['profiles'] = profiles

    return render(request, 'index.html', context_dict)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def current_user(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'user.html', {'user': user})
