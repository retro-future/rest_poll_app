from django.urls import path

from poll_app import views

urlpatterns = [
    path("polls/", views.PollsListView.as_view()),
    path("polls/<int:pk>/", views.PollDetailView.as_view()),
    path("question/<int:pk>/", views.QuestionView.as_view()),
    path("user_answers/create/", views.UACreateAndView.as_view(), name="user_answer_create"),
    path("user_answers/view/", views.UACreateAndView.as_view(), name="user_answer_view"),
    path("user_answers/update/<int:answer_id>/", views.UserAnswerUpdate.as_view(), name="user_answer_update"),
    path("user_answers/delete/<int:answer_id>/", views.UserAnswerUpdate.as_view(), name="user_answer_delete"),

]
