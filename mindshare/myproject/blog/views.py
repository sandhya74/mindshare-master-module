from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import *
from blog.serializers import *
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from django.utils.safestring import mark_safe

# Create your views here.
def home_view(request):
    return HttpResponseRedirect('/master_page')


def material_List(request):  
    
    material= Materials.objects.all()  
    return render(request,"material_list.html",{'material':material})  

def master_Page(request):
    material=Materials.objects.all()
    return render(request,"master_page.html",{'material':material})    

def create_Material(request): 

    #import pdb;pdb.set_trace()
    material=Materials.objects.values_list('Material_Code', flat=True)
    materials=list(material)
    if request.method == "POST":
        form = MaterialsForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            
            form.instance.Material_Code = request.POST['Material_Code']
            form.instance.Material_Descriptions = request.POST['Material_Name']
            form.instance.Material_Location = request.POST['Material_Location']
            form.instance.Unit_of_Measurement = request.POST['Unit_of_Measurement']
            form.instance.Maximum_Level = request.POST['Maximum_Level']
            form.instance.Minimum_Level = request.POST['Minimum_Level']
            form.instance.Re_order_Level = request.POST['Re_order_Level']
            form.instance.Quantity=request.POST['Quantity']
           
            form.save()
                
            return HttpResponseRedirect('/material_list')
        
        
        else:
            print(form.errors)
    else:
        form = MaterialsForm()
        return render(request,'create_material.html',{'form':form,'materials':materials})  

def material_Update(request,id):  
    

    material = Materials.objects.get(id=id)
    
    form = MaterialsForm(initial={'Material_Code':material.Material_Code, 'Material_Name': material.Material_Name
    , 
    'Material_Location': material.Material_Location, 'Unit_of_Measurement': material.Unit_of_Measurement,'Maximum_Level':material.Maximum_Level,
    'Minimum_Level':material.Minimum_Level,'Re_order_Level':material.Re_order_Level,'Quantity':material.Quantity})
    
    if request.method == "POST":  
        form = MaterialsForm(request.POST,instance=material)  
        
        if form.is_valid(): 

            try:  
                form.save() 
                return HttpResponseRedirect('/material_list')  
               
            except Exception as e: 
                return Response(status=404)   
    
    else:  
             
        return render(request,'create_material.html',{'form':form,'mat_id':material.id,'material':material}) 
        
def material_View(request,id):
    #import pdb;pdb.set_trace()
    material= Materials.objects.get(id=id)
    transaction=Transactions.objects.filter(Material_Name_id)

    return render(request,"main_list.html",{'material':material,'transaction':transaction}) 
    
    

def display(request):  
    transact= Transactions.objects.all()
    context = {'transact':transact} 
    return render(request,"transact_list.html", context ) 


def Create_Method(request):
    #import pdb; pdb.set_trace()
    doc_unique=Transactions.objects.values_list('Document_Number', flat=True)
    doc_unique=list(doc_unique)
    material_name=Materials.objects.all()
    # results=MaterialsInventory.objects.all()
    mydict={}
    
    for data in material_name:
        mydict[data.Material_Name] = data.Quantity;
   
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
    
        form = TransactionForm(request.POST)
        
        
        
        saverecord=Transactions()
        saverecord.Transaction_Type=request.POST.get('Transaction_Type')
        print(saverecord.Transaction_Type)
        
        if request.POST.get('Received_From') == '':
            saverecord.Received_From = None
        else:
            saverecord.Received_From=request.POST.get('Received_From')
        if request.POST.get("Number_Of_Received") =='':
            saverecord.Number_Of_Received = None
        else:
            saverecord.Number_Of_Received=request.POST.get("Number_Of_Received")
    
        if request.POST.get('Issue_To') == '':
            saverecord.Issue_To = None
        else:
            
            saverecord.Issue_To=request.POST.get('Issue_To')

        if request.POST.get("Number_Of_Issued") =='':
            saverecord.Number_Of_Issued = None
        else:
            no_of_issued = request.POST.get("Number_Of_Issued")
            saverecord.Number_Of_Issued= int(no_of_issued)
        saverecord.Balance=request.POST.get('Balances')    
        print(saverecord.Balance)
        saverecord.Material_Name=request.POST.get('Material_Name')
        saverecord.Date=request.POST.get('Date')
        saverecord.Document_Number=request.POST.get('Document_Number')
        saverecord.Verification_Date=request.POST.get('Verification_Date')
        saverecord.Verified_By=request.POST.get('Verified_By')
        saverecord.save()
        # print(saverecord)
        return redirect('/display')
        
    else:
        # form = MaterialForm.objects.all(),{"mat":form}
        return render(request, 'create_transact.html',{'mat_name':material_name,'TransactInventory':mydict,'doc_id':doc_unique})



def update(request, id):
    
	# import pdb;pdb.set_trace()
	transact = Transactions.objects.get(id=id)
	form = TransactionForm(instance=transact)

	if request.method == 'POST':
		form = TransactionForm(request.POST, instance=transact)
		if form.is_valid():
			form.save()
			return redirect('/display')
	mat =  Transactserializers(transact).data
	context = {'form':form,'id':transact.id,'mat':mat}
	# print("------",material)    
	return render(request, 'create_transact.html', context)