# Generated by Django 4.1.1 on 2022-10-07 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0005_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Customer',
        ),
    ]
