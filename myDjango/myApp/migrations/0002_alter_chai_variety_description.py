# Generated by Django 5.1.7 on 2025-03-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chai_variety',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
