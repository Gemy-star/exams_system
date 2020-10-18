from django.db import models
from django.urls import reverse
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='الإسم', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name='وصف ', blank=True, null=True)
    picture = models.ImageField(null=True, blank=True, verbose_name='الصوره')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Question(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(default=0)
    question = models.TextField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    choose = [('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4')]
    answer = models.CharField(max_length=1, choices=choose)

    def __str__(self):
        return str(self.question)

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Exam(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ques = models.ManyToManyField(Question)
    no_of_question = models.Count(Question.question)
    cat_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'


class FinalResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'FinalResult'
        verbose_name_plural = 'FinalResults'
