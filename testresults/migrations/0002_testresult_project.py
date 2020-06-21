# Generated by Django 2.2.5 on 2020-06-21 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20200622_0037'),
        ('testresults', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Project'),
        ),
    ]
