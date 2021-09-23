from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def index(request):
  message = "Welcome to Rate-My-Project"
  return render(request,'index.html',{"message": message})


def register_new_user(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, 'Registration Successful.')
      return redirect('homepage')
    messages.error(request, 'Unsuccessful registration. Invalid information.')
  form = NewUserForm()
  return render(request, 'registration/registration_form.html', {"registration_form": form} )

