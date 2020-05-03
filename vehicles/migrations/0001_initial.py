# Generated by Django 3.0.5 on 2020-04-29 12:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('car_reg_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('car_make', models.CharField(max_length=100)),
                ('car_type', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('hash', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'vehicles',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('previous_hash', models.CharField(max_length=100)),
                ('hash', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('car_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_transactions', to='vehicles.Vehicles')),
                ('kra', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_transactions', to='users.Agent')),
                ('national', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_transactions', to='users.Owner')),
            ],
            options={
                'db_table': 'vehicle_transactions',
            },
        ),
    ]
