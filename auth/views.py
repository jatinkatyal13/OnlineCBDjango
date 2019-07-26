from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# User.objects.create_user(username, email, password, first_name, last_name)

# Create your views here.
def login_view(request):
  error = ""
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user:
      login(request, user)
      return HttpResponseRedirect('/')
    else:
      error = "Incorrect Username or Password"

  context = {
    "error": error
  }
  return render(request, 'auth/login.html', context)

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/auth/login')
