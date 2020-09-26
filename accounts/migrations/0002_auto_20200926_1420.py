# Generated by Django 3.1.1 on 2020-09-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Owner', 'Owner'), ('Executive', 'Executive'), ('Employee', 'Employee')], max_length=50, null=True),
        ),
    ]
