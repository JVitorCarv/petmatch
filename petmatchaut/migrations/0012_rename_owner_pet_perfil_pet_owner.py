# Generated by Django 4.0.4 on 2022-05-07 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petmatchaut', '0011_alter_pet_perfil_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet_perfil',
            old_name='owner',
            new_name='pet_owner',
        ),
    ]
