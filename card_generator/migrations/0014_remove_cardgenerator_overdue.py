# Generated by Django 4.1.4 on 2022-12-11 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_generator', '0013_cardgenerator_overdue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardgenerator',
            name='overdue',
        ),
    ]
