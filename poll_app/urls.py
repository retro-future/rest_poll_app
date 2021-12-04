from django.urls import path

from poll_app import views

urlpatterns = [
    path("polls/", views.PollsListView.as_view()),
    path("polls/<int:pk>/", views.PollDetailView.as_view()),
    path("question/<int:pk>/", views.QuestionView.as_view()),
]