# Generated by Django 2.2.5 on 2019-09-13 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='categories',
        ),
    ]
