# Generated by Django 4.0.3 on 2022-04-07 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_articles_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='date',
        ),
    ]
