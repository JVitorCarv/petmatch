# Generated by Django 4.0.4 on 2022-05-06 01:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petmatchaut', '0005_remove_abstractuser_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AbstractUser',
            new_name='ProfileInfo',
        ),
    ]
