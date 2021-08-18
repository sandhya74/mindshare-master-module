# Generated by Django 2.0 on 2021-08-05 07:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_transaction_material_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('doc_no', models.IntegerField(unique=True)),
                ('received_from', models.CharField(blank=True, max_length=200, null=True)),
                ('issue', models.CharField(blank=True, max_length=200, null=True)),
                ('balance', models.IntegerField()),
                ('verification_date', models.DateField()),
                ('verified_by', models.CharField(max_length=100)),
                ('material_code', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Materials')),
            ],
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]