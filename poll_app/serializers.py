from rest_framework import serializers

from poll_app.models import Poll, Question, Answer, UserAnswers


class CurrentUserDefault:
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


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
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=CurrentUserDefault())
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field="id")
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field="id")
    answer = serializers.SlugRelatedField(queryset=Answer.objects.all(), slug_field="id")

    class Meta:
        model = UserAnswers
        fields = ("id", "user_id", "poll", "question", "answer")

    def create(self, validated_data):
        return UserAnswers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value, in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        print(attrs)
        try:
            obj = UserAnswers.objects.get(user_id=attrs['user_id'], poll=attrs['poll'],
                                          question=attrs['question'], answer=attrs['answer'])
        except UserAnswers.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError("Already answered")
