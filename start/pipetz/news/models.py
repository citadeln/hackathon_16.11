from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс новости', max_length=250)
    full_text = models.TextField('Полный текст новости')
    image = models.ImageField('Изображение', upload_to='uploads/img/', default=None)
    date = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'