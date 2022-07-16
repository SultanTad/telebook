from django.db import models


class TypesInPhone(models.Model):

    types = models.CharField(max_length=50, verbose_name='Типы номеров')

    def __str__(self):
        return f'{self.types}'

    class Meta:
        verbose_name = 'Тип номера'
        verbose_name_plural = 'Типы номеров'


class ContactInPhone(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    numbers = models.PositiveBigIntegerField(verbose_name='номер')
    types_in_phone = models.ForeignKey(TypesInPhone, on_delete=models.CASCADE, verbose_name='Тип номера',
                                       default='Выберите тип')

    def __str__(self):
        return f'{self.surname}  {self.name}  {self.patronymic}'

    class Meta:
        verbose_name = 'Имя в телефонной книге'
        verbose_name_plural = 'Имена в телефонной книге'
