# Generated by Django 3.2.5 on 2022-06-09 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listing_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentId',
            new_name='comment_id',
        ),
    ]