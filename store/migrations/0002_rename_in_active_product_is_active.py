# Generated by Django 4.0.5 on 2022-11-26 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='in_active',
            new_name='is_active',
        ),
    ]
