# Generated by Django 4.0.5 on 2022-07-11 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Имя в телефонной книге',
                'verbose_name_plural': 'Имена в телефонной книге',
            },
        ),
        migrations.CreateModel(
            name='TypesInPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.PositiveBigIntegerField(choices=[(None, 'Выбрать тип'), (1, 'Мобильный'), (2, 'Домашний'), (3, 'Рабочий'), (4, 'Личный'), (5, 'почта')], default=1, verbose_name='Тип скидки')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testtelebook.contactinphone', verbose_name='Полное имя')),
            ],
            options={
                'verbose_name': 'Тип номера',
                'verbose_name_plural': 'Типы номеров',
            },
        ),
    ]
