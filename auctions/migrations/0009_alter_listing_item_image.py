# Generated by Django 3.2.5 on 2022-06-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_listid_listing_list_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='item_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
