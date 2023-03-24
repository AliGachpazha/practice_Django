from .forms import UserForms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    form = UserForms()
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return True

    return render(request, 'user/html/register.html', {'form': form})


def login():
    pass
