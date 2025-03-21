from django.shortcuts import render
from .forms import ChaiVerityForms 
from .models import Chaiverity ,store
from django.shortcuts import get_object_or_404
# Create your views here.

def chai(request):
    chais=Chaiverity.objects.all()
    return render(request, 'chai/all_chai.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai =get_object_or_404(Chaiverity,pk=chai_id)
    return render(request, 'chai/chai_detail.html',{'chai':chai})




def chai_allstore(request):
    stores = None
    form = ChaiVerityForms()  # Form initialize karna zaroori hai

    if request.method == "POST":
        form = ChaiVerityForms(request.POST)
        if form.is_valid():
            chai_verity = form.cleaned_data['Chai_verity']
            stores = store.objects.filter(chai_Chaiverity=chai_verity)  # Store model ka correct reference diya

    return render(request, 'chai/all_store.html', {'stores': stores, 'form': form})  # Ensure response always returned