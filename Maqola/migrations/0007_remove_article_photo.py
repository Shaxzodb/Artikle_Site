# Generated by Django 3.2.5 on 2021-07-06 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maqola', '0006_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
    ]
