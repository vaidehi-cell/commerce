# Generated by Django 3.2.5 on 2022-06-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
