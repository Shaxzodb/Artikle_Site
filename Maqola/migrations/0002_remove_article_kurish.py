# Generated by Django 3.2.2 on 2008-12-31 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maqola', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='kurish',
        ),
    ]