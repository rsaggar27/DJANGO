from django.shortcuts import render
from .models import Chai_Variety,ChaiStore
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm
# Create your views here.

def first_page(request):
    chais= Chai_Variety.objects.all()
    return render(request,'myApp/app-first.html',{'chais':chais })

def chai_detail(request,chai_id):
    chai=get_object_or_404(Chai_Variety,pk=chai_id)
    return render(request,'myApp/chai-detail.html',{'chai':chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = ChaiStore.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()

    return render(request, 'myApp/chai_stores.html', {'form': form, 'stores': stores})




