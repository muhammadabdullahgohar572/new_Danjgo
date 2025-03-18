from django.shortcuts import render

from .models import Chaiverity
from django.shortcuts import get_object_or_404
# Create your views here.

def chai(request):
    chais=Chaiverity.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai =get_object_or_404(Chaiverity,pk=chai_id)
    return render(request, 'chai/chai_detail.html',{'chai':chai})