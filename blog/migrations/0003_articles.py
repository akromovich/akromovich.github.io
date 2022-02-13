# Generated by Django 4.0.2 on 2022-02-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_work_alter_post_photo_alter_post_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.CharField(max_length=300, verbose_name='Текст')),
            ],
        ),
    ]