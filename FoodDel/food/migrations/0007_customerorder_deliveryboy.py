# Generated by Django 3.1.6 on 2021-02-10 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_customerorder_orderprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='deliveryboy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.deliveryprofile'),
        ),
    ]
