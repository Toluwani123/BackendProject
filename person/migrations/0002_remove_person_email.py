# Generated by Django 4.1.1 on 2022-10-11 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
    ]
