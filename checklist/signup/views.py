from django.shortcuts import render
from .forms import SignUpForm
from .models import User
from django.http import HttpResponseRedirect

def home(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User (
                username = form.cleaned_data.get("name"),
                password = form.cleaned_data.get("password"),
                email = form.cleaned_data.get("email")
            )
            user.save()
            return HttpResponseRedirect("../#")

    form = SignUpForm()
    return render(request, "signup.html", {"form":form})
