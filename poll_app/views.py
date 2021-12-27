import answers as answers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from poll_app.models import Poll, Question, UserAnswers, Answer
from poll_app.serializers import QuestionSerializer, PollSerializer, UserAnswersSerializer, AnswerSerializer


class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        question.delete()
        return Response("Question deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def poll_view(request):
    poll = Poll.objects.all()
    serializer = PollSerializer(poll, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def active_poll_view(request):
    survey = Poll.objects.filter(end_time__gte=timezone.now()).filter(start_time__lte=timezone.now())
    serializer = PollSerializer(survey, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated, IsAdminUser))
def poll_create(request):
    serializer = PollSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class PollUpdateAndDelete(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def patch(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        poll.delete()
        return Response("Poll deleted.", status=status.HTTP_204_NO_CONTENT)


class AnswerView(APIView):
    """
    Create Update and Delete Answer
    """
    permission_classes = (IsAuthenticated, IsAdminUser)

    def delete(self, request, answer_id):
        answer = get_object_or_404(Answer, pk=answer_id)
        answer.delete()
        return Response("Answer deleted", status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, answer_id):
        answer = get_object_or_404(Answer, pk=answer_id)
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UACreateAndListView(APIView):
    """
    List and Create User Answers
    """

    def get(self, request):
        user_answers = UserAnswers.objects.filter(user_id=request.user.id)
        serializer = UserAnswersSerializer(user_answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAnswersSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAnswerUpdate(APIView):
    """
    Delete and Update User Answers
    """
    permission_classes = (IsAuthenticated, IsAdminUser)

    def patch(self, request, answer_id):
        answer = get_object_or_404(UserAnswers, pk=answer_id)
        serializer = UserAnswersSerializer(answer, data=request.data, context={"request": request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_id):
        answer = get_object_or_404(UserAnswers, pk=answer_id)
        answer.delete()
        return Response("UserAnswer is deleted", status=status.HTTP_204_NO_CONTENT)
