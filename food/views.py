from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    if request.method=="POST":
        food_consumed=request.POST.get("food_consumed")
        consume=Food.objects.get(name=food_consumed)
        user=request.user
        consume=Consume(user=user,food_consumed=consume)
        consume.save()
        foods=Food.objects.all()
    else:
   
        foods=Food.objects.all()
    consumed_foods=Consume.objects.filter(user=request.user)
    return render(request, "index.html", {"foods":foods,"consumed_foods":consumed_foods})