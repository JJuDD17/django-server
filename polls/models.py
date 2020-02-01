from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=500)
    post_image = models.ImageField('image', blank=True)
    pub_date = models.DateTimeField('date posted')

    def __str__(self):
        return self.post_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text