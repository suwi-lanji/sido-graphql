# Generated by Django 5.1.7 on 2025-03-12 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debtor', models.CharField(db_index=True, max_length=100)),
                ('status', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=18)),
                ('pending_balance', models.DecimalField(decimal_places=2, max_digits=18)),
                ('credit_date', models.DateField()),
                ('returned_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tenant')),
            ],
        ),
    ]
