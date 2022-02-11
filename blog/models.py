from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title=models.CharField(max_length=200,blank=False,verbose_name='Название статьи')
    text=RichTextUploadingField(max_length=1000,blank=False,verbose_name='текст')
    photo = models.ImageField(upload_to='post_images',null=True,blank=True,verbose_name="выбрать фото")

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=30,verbose_name="Имя фамилие работающих людей")
    totle = models.CharField(max_length=50,verbose_name="должность")
    photo = models.ImageField(upload_to='post_images',null=False,blank=False,verbose_name="Фоторафия сотрудника")

    def __str__(self):
        return self.title