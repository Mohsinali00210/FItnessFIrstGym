# Generated by Django 4.2.5 on 2023-09-09 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('PhoneNo', models.CharField(max_length=11)),
                ('Email', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=150)),
                ('DateOfBirth', models.DateField()),
                ('Gender', models.CharField(max_length=100)),
                ('LockerAssignment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FitnessGoals', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='images/')),
                ('PersonId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.person')),
            ],
        ),
    ]
