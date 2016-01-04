from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()
    var = {
        'form': form
    }
    return render(request, "login.html", var)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
