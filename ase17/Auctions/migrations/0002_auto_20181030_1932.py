# Generated by Django 2.1.2 on 2018-10-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_details',
            name='category',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='item_details',
            name='item_name',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
