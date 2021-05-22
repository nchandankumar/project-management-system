from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from . models import Technology,Category
from django.db.models import Sum
from .forms import *
# from .forms import CalciForm

def Cost(request):
    catg = Category.objects.all()
    tech = Technology.objects.all()
    context= {
        'catg':catg,
        'tech':tech,
    }
    return render(request,'calculator/cost.html',context)

def Addtech(request,tech_id):
    tech1 = Technology.objects.filter(id=tech_id).first()
    price = tech1.price
    post=AddTech()
    post.name=tech1
    post.price = price
    post.save()
    add = AddTech.objects.all()
    count= AddTech.objects.all().count()
    sum = AddTech.objects.aggregate(Sum('price'))
    ans= sum['price__sum']
    context= {
        'add':add,
        'count':count,
        'ans':ans,

    }
    return render(request,'calculator/addusertech.html',context)

def Done(request):
    tech=AddTech.objects.all()
    tech.delete()
    
    return redirect('calculator:cost')

