# Generated by Django 3.2.6 on 2021-12-03 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='in_reply_to_user',
        ),
    ]
