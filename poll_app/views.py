from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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


class UserAnswersList(APIView):
    """
    list of user answers
    """
    def get(self, request):
        print(request.user.id)
        user_answers = UserAnswers.objects.all()
        serializer = UserAnswersSerializer(user_answers, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = {"user_id": request.user.id, "answer_id": request.data.get("user_id")}
        serializer = UserAnswersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(data={"answer": "ok"}, safe=False)
