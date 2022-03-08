from django.shortcuts import render
from django.http import HttpResponse
from .models import Something, Item

# Create your views here.

def index(res, id):
  s = Something.objects.get(id=id)
  item = s.item_set.get(id=1)
  return HttpResponse("<h1>yo %s</h1><br></br><p>%s hah</p>" %(s.name, str(item.text)))
