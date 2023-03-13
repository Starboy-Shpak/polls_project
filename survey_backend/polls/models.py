from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Poll(models.Model):
    title = models.CharField('Название опроса', max_length=256, unique=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField('Текст вопроса', max_length=4000)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        constraints = (
            UniqueConstraint(
                fields=('poll', 'text', ),
                name='unique_question',
            ),
        )

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
    # points = models.PositiveIntegerField('Баллы', default=0)

    class Meta:
        verbose_name_plural = 'Баллы пользователей'
        constraints = (
            UniqueConstraint(
                fields=('question', 'user', ),
                name='unique_point',
            ),
        )
