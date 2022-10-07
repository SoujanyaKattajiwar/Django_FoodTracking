from django.shortcuts import render
from .models import Food,Consume
# Create your views here.
def index(request):
    if request.method=="POST":
        consumed_food=request.POST['food_consumed']
        food=Food.objects.get(name=consumed_food)
        user=request.user
        consume=Consume(food_consumed=food,user=user)
        consume.save()
        food = Food.objects.all()
        consumed_food = Consume.objects.filter(user=request.user)
    else:
        food=Food.objects.all()
        consumed_food=Consume.objects.filter(user=request.user)
    return render(request,"myapp/index.html",{'food':food,'consumed_food':consumed_food})
