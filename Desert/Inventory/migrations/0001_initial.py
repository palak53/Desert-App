# Generated by Django 3.1.5 on 2023-04-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('stock_quantity', models.IntegerField()),
                ('needs_reorder', models.BooleanField(default=False)),
            ],
        ),
    ]
