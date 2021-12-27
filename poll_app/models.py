from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT, related_name="questions")

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return self.text


class UserAnswers(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name="poll", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name="answer", on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        text = f"{self.user_id} --- {self.answer}"
        return text
