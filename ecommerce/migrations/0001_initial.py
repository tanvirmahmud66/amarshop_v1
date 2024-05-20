# Generated by Django 4.2.10 on 2024-05-15 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product')),
            ],
        ),
    ]