from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm, ProfileForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  message = "Welcome to Rate-My-Project"
  return render(request,'index.html',{"message": message})


def register_user(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, f'Registration Successful.')
      return redirect('homepage')
    messages.error(request, f'Unsuccessful registration. Invalid information.')
  form = NewUserForm()
  return render(request, 'registration/registration_form.html', {"registration_form": form})


def login_user(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('homepage')
      else:
        messages.error(request, f'Invalid Username or password')
    else:
      messages.error(request, f'Invalid username or password')
  form = AuthenticationForm()
  return render(request, 'registration/login_form.html', {"login_form": form})

def logout_user(request):
  logout(request)
  messages.info(request, f'You have successfully logged out.')
  return redirect('login')


def profile(request,user_id):
  user = User.objects.get(pk=user_id)
  user.save()
  return render(request,'profile/profile.html', {"user": user})

@login_required
@transaction.atomic
def update_profile(request):
  if request.method == 'POST':
    user_form = NewUserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save
      profile = profile_form.save()
      messages.success(request,f'Your profile was successfully updated!')
      return redirect('homepage')
    else:
      messages.error(request,f'Please try updating your profile again.')
  else:
    user_form = NewUserForm()
    profile_form = ProfileForm()
  return render(request,'profile/update_profile.html',{"profile_form":profile_form, "user_form": user_form})

