from django.urls import path

from .views import IndexView, AboutAuthorView, QuestionView, ResultsView, vote, UsersListView, ProfileView, poll_detail

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users', UsersListView.as_view(), name='users'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('<int:poll_id>/', poll_detail, name='poll_detail'),
    path('<int:pk>/questions', QuestionView.as_view(), name='questions'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('author/', AboutAuthorView.as_view(), name='author'),
]
