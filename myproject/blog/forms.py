from django import forms
from django.forms import ModelForm
from blog.models import *
from blog.views import *
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages 
class MaterialsForm(forms.ModelForm):
    #import pdb;pdb.set_trace()
    class Meta:
        model=Materials
        
        fields=( 
            
        'Material_Code',
        'Material_Name',
        'Material_Location',
        'Unit_of_Measurement',
        'Maximum_Level',
        'Minimum_Level',
        'Re_order_Level',
        'Quantity')
    
    
    # def clean_Material_Code(self):
    #     import pdb;pdb.set_trace()
    #     #form = MaterialsForm(request.POST)
    #     Material_Code = self.cleaned_data.get('Material_Code')
    #     for instance in Materials.objects.all():
    #         if instance.Material_Code == Material_Code:
    #             return forms.ValidationError('This material_code is already created',Material_Code)
               
    #     return Material_Code
        
      
            		
            



	
