# Generated by Django 2.2.5 on 2020-06-21 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_delete_producttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='capacities',
        ),
        migrations.RemoveField(
            model_name='project',
            name='nand_types',
        ),
        migrations.RemoveField(
            model_name='project',
            name='soc_types',
        ),
    ]
