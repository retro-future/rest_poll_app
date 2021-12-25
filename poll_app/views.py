import answers as answers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from poll_app.models import Poll, Question, UserAnswers
from poll_app.serializers import PollsListSerializer, QuestionSerializer, PollDetailSerializer, UserAnswersSerializer


class PollsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Poll.objects.all()
    serializer_class = PollsListSerializer


class QuestionView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PollDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollDetailSerializer


class UACreateAndView(APIView):
    """
    list and create User Answers
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
    delete and update User Answers
    """
    permission_classes = (IsAuthenticated, IsAdminUser)

    def patch(self, request, answer_id):
        answer = get_object_or_404(UserAnswers, pk=answer_id)
        serializer = UserAnswersSerializer(answer, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, answer_id):
        answer = get_object_or_404(UserAnswers, pk=answer_id)
        answer.delete()
        return Response("UserAnswer is deleted", status=status.HTTP_204_NO_CONTENT)
