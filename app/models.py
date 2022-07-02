from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from embed_video.fields import EmbedVideoField


class Lecture(models.Model):
    name = models.CharField(max_length=20)
    time = models.IntegerField()
    video = EmbedVideoField()

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=20)
    question = models.CharField(max_length=100)
    op1 = models.CharField(max_length=40, null=True)
    op2 = models.CharField(max_length=40, null=True)
    op3 = models.CharField(max_length=40, null=True)
    answer = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.name

    related_lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)


class QuizLecture(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)


class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    generated_on = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
