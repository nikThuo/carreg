# Generated by Django 3.0.5 on 2020-04-07 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Roles',
            fields=[
                ('role_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_role',
            },
        ),
        migrations.CreateModel(
            name='User_Type',
            fields=[
                ('user_type_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User_Roles')),
            ],
            options={
                'db_table': 'user_type',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('national_id', models.IntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('kra_pin', models.CharField(max_length=100)),
                ('pwd', models.CharField(default='', max_length=100)),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User_Type')),
            ],
            options={
                'db_table': 'owners',
            },
        ),
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pwd', models.CharField(default='', max_length=100)),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User_Type')),
            ],
            options={
                'db_table': 'authority',
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('kra_pin', models.CharField(max_length=100)),
                ('pwd', models.CharField(default='', max_length=100)),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User_Type')),
            ],
            options={
                'db_table': 'agents',
            },
        ),
    ]
