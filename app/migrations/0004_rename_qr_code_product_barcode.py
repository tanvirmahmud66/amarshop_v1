# Generated by Django 4.2.10 on 2024-04-29 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_qr_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='qr_code',
            new_name='barcode',
        ),
    ]
