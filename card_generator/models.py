from django.db import models


class CardGenerator(models.Model):
    card_series = models.CharField(max_length=50, verbose_name='Серия карты')
    number_card = models.IntegerField(verbose_name='Номер карты')
    card_issue_date = models.DateTimeField(db_index=True, verbose_name='Дата выпуска карты')
    end_date_of_card_activity = models.DateTimeField(db_index=True, verbose_name='Дата окончания активности карты')
    card_activation_date = models.DateTimeField(db_index=True, verbose_name='Дата активации карты')
    amount_on_the_card = models.FloatField(verbose_name='Сумма на карте')
    TYPE = (
        ('not_activated', 'Не активирована'),
        ('activated', 'Активирована'),
        ('overdue', 'Просрочена'),
    )
    card_status = models.CharField(max_length=50, choices=TYPE, verbose_name='Статус карты')

    def __str__(self):
        return self.number_card

    class Meta:
        verbose_name_plural = 'Карты'
        verbose_name = 'Карты'
        ordering = ['-card_issue_date']
