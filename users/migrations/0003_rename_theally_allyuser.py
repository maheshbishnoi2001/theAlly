# Generated by Django 4.1.7 on 2023-02-25 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_theally_delete_users"),
    ]

    operations = [
        migrations.RenameModel(old_name="theAlly", new_name="allyuser",),
    ]
