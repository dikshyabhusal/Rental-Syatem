# Generated by Django 5.1.1 on 2024-09-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField(default=0)),
                ('car_name', models.CharField(default='', max_length=30)),
                ('car_desc', models.CharField(default='', max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='car/images')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('cars', models.CharField(default='', max_length=50)),
                ('days_for_rent', models.IntegerField(default=0)),
                ('date', models.CharField(default='', max_length=50)),
                ('loc_from', models.CharField(default='', max_length=50)),
                ('loc_to', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
