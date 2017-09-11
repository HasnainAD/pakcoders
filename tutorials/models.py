from django.db import models


class TutorialModel(models.Model):
    def __str__(self):
        return self.tutorialName
    tutorialName = models.CharField(max_length=200)
    date = models.DateTimeField('date published')


class ArticleModel(models.Model):
    def __str__(self):
        return self.articleName
    articleName = models.CharField(max_length=200)
    tutorial = models.ForeignKey(TutorialModel, on_delete=models.CASCADE)

