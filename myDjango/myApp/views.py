from django.shortcuts import render
from .models import Chai_Variety
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.

def first_page(request):
    chais= Chai_Variety.objects.all()
    return render(request,'myApp/app-first.html',{'chais':chais })

def chai_detail(request,chai_id):
    chai=get_object_or_404(Chai_Variety,pk=chai_id)
    return render(request,'myApp/chai-detail.html',{'chai':chai})






