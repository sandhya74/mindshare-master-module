# Generated by Django 2.0 on 2021-08-04 10:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210804_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=20)),
                ('material_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('doc_no', models.IntegerField(unique=True)),
                ('received_from', models.CharField(blank=True, max_length=200, null=True)),
                ('issue', models.CharField(blank=True, max_length=200, null=True)),
                ('balance', models.IntegerField()),
                ('verification_date', models.DateField()),
                ('verified_by', models.CharField(max_length=100)),
            ],
        ),
    ]
