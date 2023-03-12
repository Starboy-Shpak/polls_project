from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Question(models.Model):
    text = models.CharField('Текст вопроса', max_length=4000, unique=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField('Вариант ответа', max_length=500)
    votes = models.PositiveIntegerField('Голосов', default=0)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'
        constraints = (
            UniqueConstraint(
                fields=('question', 'choice', ),
                name='unique_choice',
            ),
        )

    def __str__(self):
        return self.choice


class Point(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Пользователь',
    )
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    points = models.PositiveIntegerField('Баллы', default=0)

    class Meta:
        ordering = ['points']
        # verbose_name = 'Баллы пользователей'
        verbose_name_plural = 'Баллы пользователей'

    def __str__(self):
        return f'{self.user} заработал {self.points} баллов'
