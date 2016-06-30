from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CustomUser
from .templatetags.milo_tags import eligible, bizzfuzz
import csv
from django.http import HttpResponse
from .tables import CustomUserTable
from django_tables2 import RequestConfig
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserForm


def users_list(request):
    context_dict = {}
    profiles = CustomUser.objects.all()
    table = CustomUserTable(CustomUser.objects.all())
    table.paginate(page=request.GET.get('page', 1), per_page=10)
    RequestConfig(request).configure(table)
    context_dict['table'] = table

    return render(request, 'index.html', context_dict)


def export_users(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    profiles = CustomUser.objects.all()
    for profile in profiles:
        writer.writerow([profile.username, profile.birthday, eligible(profile.birthday), profile.random_number,
                         bizzfuzz(profile.random_number)])

    return response


def current_user(request, username):
    profile = CustomUser.objects.get(username=username)

    return render(request, 'user.html', {'profile': profile})


def del_user(request, username):
    user_to_del = get_object_or_404(CustomUser, username=username)
    user_to_del.delete()
    messages.success(request, "User deleted")

    return HttpResponseRedirect("/")


def add_user(request):
    context_dict = {}

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            messages.success(request, "User created")
            return HttpResponseRedirect("/")
    else:
        form = UserForm()
    context_dict['form'] = form

    return render(request, 'add.html', {'form': form})


def edit_user(request, username):
    context_dict = {}
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            messages.success(
                request, u"User was updated"
            )
            new_item = form.save(commit=False)
            new_item.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm(instance=user)
    context_dict['form'] = form
    context_dict['object'] = user
    return render(
        request,
        'edit.html',
        context_dict,
    )
