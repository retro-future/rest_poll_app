from django.http import JsonResponse
from rest_framework import generics, permissions
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
