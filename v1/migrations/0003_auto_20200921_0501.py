# Generated by Django 3.1.1 on 2020-09-21 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_post_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]