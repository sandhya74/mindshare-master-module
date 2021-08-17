from django.test import TestCase

# Create your tests here.
from blog.models import *
from blog.views import *
from django.urls import reverse
from django.test import RequestFactory, TestCase
from rest_framework.response import Response
from django.template.defaultfilters import slugify
from django.test import Client

class MaterialTestCase(TestCase):
    
    def create_material(self,Material_Code="mc02",Material_Descriptions="harshitha", Material_Location="chennai",Unit_of_Measurement=7,Maximum_Level=2,Minimum_Level=2, Re_order_Level=2):

        return Materials.objects.create(Material_Code=Material_Code, Material_Descriptions=Material_Descriptions,Material_Location=Material_Location,Unit_of_Measurement=Unit_of_Measurement,Maximum_Level=Maximum_Level,Minimum_Level=Minimum_Level,Re_order_Level=Re_order_Level )

    def test_material_creation(self):
        w = self.create_material()
        self.assertTrue(isinstance(w, Materials))

   
    def setUp(self):
        self.factory = RequestFactory()
        self.client=Client()
    
    def test_material_List(self):
        request = self.factory.get('/material_list')    
        self.assertEqual(Response.status_code, 200)
    
    def test_create_Material_post(self):
        post=Materials.objects.create(Material_Code="mc011")
        post.Material_Descriptions="harshitha"
        post.Material_Location="chennai"
        post.Unit_of_Measurement=7
        post.Maximum_Level=2
        post.Minimum_Level=2
        post.Re_order_Level=2
        post.save()
        self.assertEqual(Response.status_code,200)
       