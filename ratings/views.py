from django.shortcuts import render

# Create your views here.
def index(request):
  message = "Welcome to Rate-My-Project"
  return render(request,'index.html',{"message": message})
