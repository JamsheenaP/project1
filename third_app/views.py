from django.shortcuts import render, HttpResponse, redirect
from third_app.models import Products

# Create your views here.
def welcome(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        description = request.POST['description']
        obj = Products(name=name, price=price,category=category,description=description)
        obj.save()
        #save code

        return render(request,"home.html")
    else:
        return render(request,"home.html")