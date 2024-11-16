from django.db import models
from django.conf import settings


class Competitions(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Описание испытаний предстоящих на соревнованиях')
    places = models.IntegerField('Количество мест для участия')
    date = models.DateTimeField('Дата проведения')

    def __str__(self):
        return self.title
    
    def reduce_places(self, count):
        """Уменьшает количество свободных мест"""
        if self.places >= count:
            self.places -= count
            self.save()
            return True
        return False

    class Meta:
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'


class Test(models.Model):
    title = models.CharField('Название теста', max_length=255)
    description = models.TextField('Описание')
    competition = models.ForeignKey(Competitions, verbose_name='Связанное соревнование', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    due_date = models.DateTimeField('Дата окончания')

    def __str__(self):
        return self.title


class Task(models.Model):
    test = models.ForeignKey(Test, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField('Заголовок задания', max_length=255)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение задания', upload_to='uploads/task_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE , null=True)
    file = models.FileField(upload_to='uploads/submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField('Оценка', null=True, blank=True)  # Добавляем поле для оценки

    def __str__(self):
        return f'{self.user.username} - {self.test.title}'
