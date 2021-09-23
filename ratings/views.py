from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import NewUserForm

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
      messages.success(request, 'Registration Successful.')
      return redirect('homepage')
    messages.error(request, 'Unsuccessful registration. Invalid information.')
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