from django import forms
from .models import Chaiverity



class ChaiVerityForms(forms.Form):
    Chai_verity = forms.ModelChoiceField(
        queryset=Chaiverity.objects.all(),
        label="Select Chai Variety"
    )