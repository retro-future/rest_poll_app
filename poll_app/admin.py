from django.contrib import admin

from poll_app.models import Answer, Poll, Question


class AnswerInline(admin.TabularInline):
    """Ответы на странице вопросов"""
    model = Answer
    extra = 1


class QuestionInline(admin.TabularInline):
    """Вопросы на странице опроса"""
    model = Question
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    """Опрос"""
    list_display = ("id", "name", "start_time", "end_time")
    list_display_links = ("name",)
    readonly_fields = ("start_time",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Вопрос"""
    list_display = ("id", "text", "question_type")
    list_display_links = ("id", "text")
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswersAdmin(admin.ModelAdmin):
    """Ответы"""
    list_display = ("id", "text")
    list_display_links = ("id", "text")
