# Generated by Django 3.2.12 on 2022-03-05 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main1', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
    ]