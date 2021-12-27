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
    path("question/create/", views.QuestionView.as_view(), name="question_create"),
    path("question/update/<int:question_id>/", views.QuestionView.as_view(), name="question_update"),
    path("question/delete/<int:question_id>/", views.QuestionView.as_view(), name="question_delete"),

    # Answer
    path('answer/create/', views.AnswerView.as_view(), name='answer_create'),
    path('answer/update/<int:answer_id>/', views.AnswerView.as_view(), name='answer_update'),
    path('answer/delete/<int:answer_id>/', views.AnswerView.as_view(), name='answer_delete'),

    # UserAnswer
    path("user_answers/create/", views.UACreateAndListView.as_view(), name="user_answer_create"),
    path("user_answers/view/", views.UACreateAndListView.as_view(), name="user_answer_view"),
    path("user_answers/update/<int:answer_id>/", views.UserAnswerUpdate.as_view(), name="user_answer_update"),
    path("user_answers/delete/<int:answer_id>/", views.UserAnswerUpdate.as_view(), name="user_answer_delete"),

]
