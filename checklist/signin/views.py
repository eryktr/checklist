from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm
# Create your views here.

def home(request):
    form = ContactForm()
    return render(request,"signin.html", {"form":form})