from django.db import models
import uuid

class Materials(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    Material_Code = models.CharField(max_length=255,blank=False,null=False,unique=True)
    Material_Name= models.CharField(max_length=255,blank=True,null=True)
    Material_Location=models.CharField(max_length=255,blank=True,null=True)
    Unit_of_Measurement=models.CharField(max_length=255,null=True, blank=True)  
    Maximum_Level=models.IntegerField(null=True, blank=True)
    Minimum_Level=models.IntegerField(null=True, blank=True)
    Re_order_Level=models.IntegerField(null=True, blank=True)
    Quantity=models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.Material_Code

class Transact(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_type=models.CharField(max_length=20)
    material_code=models.ForeignKey(Materials,on_delete=models.CASCADE,default=1)
    date=models.DateField()
    doc_no=models.IntegerField(unique=True)
    received_from=models.CharField(max_length=200,null=True,blank=True)
    receipt_no=models.IntegerField(default=0)
    issue=models.CharField(max_length=200,null=True,blank=True)
    balance=models.IntegerField()
    verification_date=models.DateField()
    verified_by=models.CharField(max_length=100)    
