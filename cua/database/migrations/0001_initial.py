# Generated by Django 4.2.5 on 2023-09-17 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('Position', models.CharField(blank=True, choices=[('Field Agent', 'Field Agent')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idNo', models.IntegerField(blank=True)),
                ('accountNo', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('branch', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=150)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.agent')),
            ],
        ),
    ]