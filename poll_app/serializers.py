from django.core.serializers import serialize
from rest_framework import serializers

from poll_app.models import Poll, Question, Answer, UserAnswers


class CurrentUserDefault:
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ("id", "text", "question")

    def validate(self, attrs):
        try:
            question = Question.objects.get(id=attrs["question"].id)
            if question.question_type == "text":
                raise serializers.ValidationError("Question id is related with 'text' type answer.")
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question id does not exists.")
        try:
            obj = Answer.objects.get(question=attrs['question'].id, text=attrs['text'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('Answer is already exists')

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field="id")
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "poll", "text", "question_type", "answers")

    def validate(self, attrs):
        question_type = attrs["question_type"]
        if question_type == "one" or question_type == "multiple" or question_type == "text":
            return attrs
        raise serializers.ValidationError("Type of question might be only 'one', 'multiple', 'text'.")

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ("id", "name", "description", "start_time", "end_time", "questions")

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "start_time" in validated_data:
            raise serializers.ValidationError({"start_time": "You can't change this field."})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserAnswersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=CurrentUserDefault())
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field="id")
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field="id")
    answer = serializers.SlugRelatedField(queryset=Answer.objects.all(), slug_field="id", allow_null=True)
    answer_text = serializers.CharField(max_length=200, allow_null=True, required=False)

    class Meta:
        model = UserAnswers
        fields = ("id", "user_id", "poll", "question", "answer", "answer_text")

    def create(self, validated_data):
        return UserAnswers.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value, in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs["question"].id).question_type
        try:
            if question_type == "one" or question_type == "text":
                obj = UserAnswers.objects.get(user_id=attrs['user_id'], poll=attrs['poll'],
                                              question=attrs['question'].id)
            elif question_type == "multiple":
                obj = UserAnswers.objects.get(question=attrs["question"].id, poll=attrs["poll"],
                                              user_id=attrs["user_id"],
                                              answer=attrs["answer"])
        except UserAnswers.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError("Already answered")
