# Generated by Django 2.0 on 2021-08-05 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='material_name',
        ),
        migrations.AddField(
            model_name='transaction',
            name='material_code',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.Materials'),
        ),
    ]
