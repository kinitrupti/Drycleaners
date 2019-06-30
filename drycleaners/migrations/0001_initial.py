# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address1', models.CharField(blank=True, max_length=256)),
                ('address2', models.CharField(blank=True, max_length=256)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zip', models.CharField(blank=True, max_length=12)),
                ('email', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='expense/')),
                ('displayname', models.CharField(max_length=128)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drycleaners.Expense')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drycleaners.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='invoice/')),
                ('displayname', models.CharField(max_length=128)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drycleaners.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drycleaners.Invoice')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drycleaners.Invoice'),
        ),
    ]
