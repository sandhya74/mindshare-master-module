# Generated by Django 2.0 on 2021-08-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210805_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='material_code',
        ),
    ]