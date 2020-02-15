from django.db import models
from django.utils import timezone


class Article(models.Model):
    header = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return repr(self.header)

    def __str__(self):
        return str(self.header)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
