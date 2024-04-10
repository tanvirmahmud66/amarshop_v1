# Generated by Django 4.2.10 on 2024-04-09 19:50

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=app.models.profile_image_path)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='GeneralUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.PositiveIntegerField(blank=True, null=True)),
                ('unit_cost', models.PositiveIntegerField()),
                ('total_cost', models.PositiveBigIntegerField(blank=True, null=True)),
                ('valuation', models.PositiveBigIntegerField(blank=True, null=True)),
                ('profit', models.PositiveBigIntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('productImg', models.ImageField(blank=True, null=True, upload_to=app.models.product_image_path)),
                ('released_year', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('product_quantity', models.BigIntegerField(blank=True, null=True)),
                ('sales_date', models.DateTimeField(auto_now_add=True)),
                ('general_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.generaluser')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sales_date'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=5)),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.PositiveBigIntegerField()),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sales')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_cost', models.PositiveIntegerField()),
                ('transaction_type', models.CharField(blank=True, default='OUT', max_length=10, null=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Credit Card', 'Credit card'), ('Master Card', 'Master Card'), ('Bank Cheque', 'Bank cheque'), ('Bkash', 'Bkash'), ('Sure Cash', 'Sure Cash'), ('DBBL Mobile', 'DBBL Mobile'), ('DBBL Card', 'DBBL Card'), ('Nagad', 'Nagad'), ('UCash', 'UCash'), ('Payoneer', 'Payoneer')], max_length=50)),
                ('paid_ammount', models.PositiveBigIntegerField()),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('due_amount', models.PositiveBigIntegerField(default=0)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.supplier')),
            ],
            options={
                'ordering': ['-purchase_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductLineUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('subtotal', models.PositiveBigIntegerField(blank=True, null=True)),
                ('sale_confirm', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.inventory')),
                ('sale_reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.sales')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
