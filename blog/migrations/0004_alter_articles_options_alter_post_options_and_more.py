# Generated by Django 4.0.2 on 2022-02-11 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Коментарие', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
    ]
