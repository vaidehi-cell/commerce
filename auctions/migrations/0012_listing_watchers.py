# Generated by Django 3.2.5 on 2022-06-09 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_comment_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchers',
            field=models.ManyToManyField(related_name='watchlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
