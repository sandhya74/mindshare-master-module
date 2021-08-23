# Generated by Django 2.0 on 2021-08-23 06:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Material_Code', models.CharField(max_length=255, unique=True)),
                ('Material_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Material_Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Unit_of_Measurement', models.CharField(blank=True, max_length=255, null=True)),
                ('Maximum_Level', models.IntegerField(blank=True, null=True)),
                ('Minimum_Level', models.IntegerField(blank=True, null=True)),
                ('Re_order_Level', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Transaction_Type', models.CharField(choices=[('Received From', 'Recieved From'), ('Issued To', 'Issued To')], default='Received From', max_length=20, null=True)),
                ('Received_From', models.CharField(blank=True, max_length=200, null=True)),
                ('Number_Of_Received', models.IntegerField(blank=True, null=True)),
                ('Issue_To', models.CharField(blank=True, max_length=200, null=True)),
                ('Number_Of_Issued', models.IntegerField(blank=True, null=True)),
                ('Balance', models.IntegerField(blank=True, default=0, null=True)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Document_Number', models.IntegerField(unique=True)),
                ('Verification_Date', models.DateField(blank=True, null=True)),
                ('Verified_By', models.CharField(max_length=100)),
                ('Material_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='display', to='blog.Materials')),
            ],
        ),
    ]
