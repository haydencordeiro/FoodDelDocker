# Generated by Django 3.1.6 on 2021-03-17 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_auto_20210317_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='customerorder',
            name='addressinwords',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='typeOfPayment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.paymentcategory'),
        ),
    ]
