# Generated by Django 3.1.6 on 2021-03-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_customerorder_orderimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='orderImg',
            field=models.CharField(default='https://images.unsplash.com/photo-1498837167922-ddd27525d352?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80.jpg', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.CharField(default='https://images.unsplash.com/photo-1458642849426-cfb724f15ef7?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80', max_length=500),
        ),
        migrations.AlterField(
            model_name='shop',
            name='ShopImg',
            field=models.CharField(blank=True, default='https://images.unsplash.com/photo-1498837167922-ddd27525d352?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80.jpg', max_length=500),
        ),
    ]
