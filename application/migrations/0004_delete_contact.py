# Generated by Django 4.1.5 on 2023-08-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_desc_contact_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
