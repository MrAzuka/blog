# Generated by Django 3.1.3 on 2020-12-07 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='career_choices',
        ),
    ]
