# Generated by Django 2.1.2 on 2018-11-24 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20181116_2332'),
        ('RestAuctionPortal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentbid', models.IntegerField(default=0)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.Profile')),
            ],
        ),
        migrations.AlterField(
            model_name='currentbid',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Profile'),
        ),
    ]
