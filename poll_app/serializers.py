from rest_framework import serializers

from poll_app.models import Poll, Question, Answer, UserAnswers


class PollsListSerializer(serializers.ModelSerializer):
    """Output a list of polls"""

    class Meta:
        model = Poll
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    """Answer Output"""

    class Meta:
        model = Answer
        exclude = ("is_answer",)


class QuestionSerializer(serializers.ModelSerializer):
    """Question output"""
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "text", "question_type", "answers")


class PollDetailSerializer(serializers.ModelSerializer):
    """Detailed poll output"""

    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ("id", "name", "description", "start_time", "end_time", "questions")


class UserAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAnswers
        fields = ("id", "user_id", "answer_id")
