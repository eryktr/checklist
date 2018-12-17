from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from .forms import SignInForm

from signup.models import User


# Create your views here.

def home(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
                un = form.cleaned_data.get("username")
                pw = form.cleaned_data.get("password")
                results = User.objects.filter(username = un, password = pw)
                if len(results) > 0:
                        return HttpResponseRedirect("../#")
                
    
    form = SignInForm()
    return render(request,"signin.html", {"form":form})