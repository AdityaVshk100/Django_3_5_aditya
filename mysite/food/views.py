from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item


# Create your views here.


def index(request):
  itemlist = Item.objects.all()
  
  context = {
    'itemlist':itemlist
  }
  return render(request,'food/index.html',context)

def details(request,item_id):
  item = Item.objects.get(pk=item_id)
  
  context={
    'item':item
  }
  return render(request,'food/details.html',context)



  
