from django.urls import path

from poll_app import views

urlpatterns = [
    # Polls
    path("polls/view/", views.poll_view, name="poll_view"),
    path("polls/view/active/", views.active_poll_view, name="active_poll_view"),
    path("polls/create/", views.poll_create, name="poll_create"),
    path("polls/update/<int:poll_id>/", views.PollUpdateAndDelete.as_view(), name="poll_update"),
    path("polls/delete/<int:poll_id>/", views.PollUpdateAndDelete.as_view(), name="polls_delete"),
    path("polls/<int:pk>/", views.PollDetailView.as_view()),

    # Questions
    path("question/<int:pk>/", views.QuestionView.as_view()),

    # UserAnswer
    path("user_answers/create/", views.UACreateAndListView.as_view(), name="user_answer_create"),
    path("user_answers/view/", views.UACreateAndListView.as_view(), name="user_answer_view"),
    path("user_answers/update/<int:answer_id>/", views.UserAnswerUpdate.as_view(), name="user_answer_update"),
    path("user_answers/delete/<int:answer_id>/", views.UserAnswerUpdate.as_view(), name="user_answer_delete"),

]
