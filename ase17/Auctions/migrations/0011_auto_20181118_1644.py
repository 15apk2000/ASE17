# Generated by Django 2.1.3 on 2018-11-18 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auctions', '0010_item_item_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionbidders',
            name='auction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auctions.Auction'),
        ),
    ]
