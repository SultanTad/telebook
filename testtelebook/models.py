from django.db import models


class ContactInPhone(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')

    def __str__(self):
        return f'{self.surname}  {self.name}  {self.patronymic}'

    class Meta:
        verbose_name = 'Имя в телефонной книге'
        verbose_name_plural = 'Имена в телефонной книге'


class TypesInPhone(models.Model):
    TYPES = [
        (None, 'Выбрать тип'),
        (1, 'Мобильный'),
        (2, 'Домашний'),
        (3, 'Рабочий'),
        (4, 'Личный'),
        (5, 'почта'),
    ]

    contact = models.ForeignKey(ContactInPhone, on_delete=models.CASCADE, verbose_name='Полное имя', blank=True,
                                null=True)
    types = models.PositiveBigIntegerField(default=None, verbose_name='Тип номера', choices=TYPES)
    numbers = models.PositiveBigIntegerField(verbose_name='номер')

    def __str__(self):
        return f'{self.contact}'

    class Meta:
        verbose_name = 'Тип номера'
        verbose_name_plural = 'Типы номеров'

