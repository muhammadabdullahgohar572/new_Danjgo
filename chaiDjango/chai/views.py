from django.shortcuts import render

from .models import Chaiverity
# Create your views here.

def chai(request):
    chais=Chaiverity.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})
