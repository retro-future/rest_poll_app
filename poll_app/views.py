from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from poll_app.models import Poll, Question
from poll_app.serializers import PollsListSerializer, QuestionSerializer, PollDetailSerializer, AnswerSerializer


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

