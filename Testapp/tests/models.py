from django.db import models
from poetry.console.commands import self


class Test(models.Model):
    title = models.CharField(max_length=100, verbose_name='Test name')

    class Meta:
        verbose_name = 'Test'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name='Question text')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name='Answer text')
    is_correct = models.BooleanField(default=False, verbose_name='Is answer correct')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Answer'


class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, verbose_name='User name')
    result = models.IntegerField(default=0, verbose_name='Result')

    def __str__(self):
        return f'{self.user}:{self.test}:{self.result}%'

    class Meta:
        verbose_name = 'Result'
