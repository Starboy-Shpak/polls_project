from django.urls import path

from .views import (AboutAuthorView, IndexView, QuestionView, ResultsView,
                    UsersListView, poll_detail, profile, vote)

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users', UsersListView.as_view(), name='users'),
    path('profile/<str:username>/', profile, name='profile'),
    path('<int:poll_id>/', poll_detail, name='poll_detail'),
    path('<int:pk>/questions', QuestionView.as_view(), name='questions'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('author/', AboutAuthorView.as_view(), name='author'),
]
