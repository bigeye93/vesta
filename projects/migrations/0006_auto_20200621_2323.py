# Generated by Django 2.2.5 on 2020-06-21 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200621_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='product',
            new_name='product_tmp',
        ),
    ]
