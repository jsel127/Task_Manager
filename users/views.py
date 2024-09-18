from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data["username"]
            password = loginForm.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            else:
                return render(request, "users/login.html", {
                    "form": LoginForm(),
                    "message": "Invalid credentials. Try again."
                })
    return render(request, "users/login.html", {
        "form": LoginForm()
    })

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logout successful."
    })