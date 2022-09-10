from django.urls import path
from .views import base_views, question_views, answer_views, comment_views

app_name = 'pybo'

urlpatterns = [
    path('question/list/qna', base_views.qna_list, name='qna_list'),
    path('question/list/bug', base_views.bug_list, name='bug_list'),
    path('<int:question_id>', base_views.detail, name='detail'),

    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>', question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>', question_views.question_vote, name='question_vote'),

    path('answer/create/<int:question_id>', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>', answer_views.answer_vote, name='answer_vote'),
]
