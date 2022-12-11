# Generated by Django 4.1.4 on 2022-12-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_generator', '0012_alter_cardgenerator_card_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardgenerator',
            name='overdue',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cardgenerator',
            name='card_status',
            field=models.CharField(choices=[('Не активирована', 'Не активирована'), ('Активирована', 'Активирована')], max_length=50, verbose_name='Статус карты'),
        ),
    ]