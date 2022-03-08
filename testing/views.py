from django.shortcuts import render
from django.http import HttpResponse
from .models import Something, Item

# Create your views here.

def index(res, id):
  s = Something.objects.get(id=id)
  return render(res, "testing/base.html", {})

def home(res):
  return render(res, "testing/home.html", {})