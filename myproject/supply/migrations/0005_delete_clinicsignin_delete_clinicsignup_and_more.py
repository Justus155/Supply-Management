# Generated by Django 5.2.3 on 2025-06-25 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_distributor_clinic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='clinicSignIn',
        ),
        migrations.DeleteModel(
            name='ClinicSignUp',
        ),
        migrations.DeleteModel(
            name='DistributorSignIn',
        ),
        migrations.DeleteModel(
            name='DistributorSignUp',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
