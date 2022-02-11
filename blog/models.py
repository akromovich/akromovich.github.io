from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title=models.CharField(max_length=200,blank=False,verbose_name='Название статьи')
    text=RichTextUploadingField(max_length=1000,blank=False,verbose_name='текст')
    photo = models.ImageField(upload_to='post_images',null=True,blank=True,verbose_name="выбрать фото")

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=30,verbose_name="Имя фамилие работающих людей")
    totle = models.CharField(max_length=50,verbose_name="должность")
    photo = models.ImageField(upload_to='post_images',null=False,blank=False,verbose_name="Фоторафия сотрудника")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.title

class Articles(models.Model):
    title = models.CharField(max_length=30,verbose_name="имя пользователя")
    email = models.EmailField(verbose_name="Email")
    text = models.CharField(max_length=300,verbose_name="Текст")

    class Meta:
        verbose_name = 'Коментарие'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.title