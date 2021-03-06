# Generated by Django 3.2.5 on 2022-06-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_remove_user_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bids',
            field=models.ManyToManyField(to='auctions.Bid'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(to='auctions.Comment'),
        ),
    ]
