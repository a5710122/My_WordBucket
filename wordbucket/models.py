from datetime import datetime
from django.db import models
from django.utils import timezone

class Word(models.Model):
    #word (text)
    word = models.TextField(default='')
    date_pub = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.word
    def was_published_recently(self):
        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)

class Explanation(models.Model):
    #foreign key
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    explanation_text = models.CharField(max_length=600)
    def __str__(self):
        return self.explanation_text

class Like_and_dislike(models.Model):
    #foreign key for Like and Dislike
    explanation = models.ForeignKey(Explanation, on_delete=models.CASCADE)
    #votes count
    votes_like = models.IntegerField(default=0)
    votes_dislike = models.IntegerField(default=0)
    def __str__(self):
        return self.votes_like
    def __str__(self):
        return self.votes_dislike
