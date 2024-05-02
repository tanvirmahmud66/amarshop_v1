# Generated by Django 4.2.10 on 2024-04-30 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_cost_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='product_quantity',
            new_name='total_quantity',
        ),
        migrations.RemoveField(
            model_name='productlineup',
            name='token',
        ),
        migrations.RemoveField(
            model_name='sales',
            name='amount',
        ),
        migrations.AddField(
            model_name='productlineup',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sales',
            name='due',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='grand_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='paid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Due', 'Due'), ('Partial', 'Partial')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='status',
            field=models.CharField(blank=True, choices=[('Delivered', 'Delivered'), ('Ordered', 'Ordered'), ('Pending', 'Pending')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productlineup',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]