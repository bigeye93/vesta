# Generated by Django 2.2.5 on 2020-06-30 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200630_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.CustomerType'),
        ),
    ]