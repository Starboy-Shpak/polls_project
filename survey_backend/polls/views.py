from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .models import Poll, Question, Choice, Point

User = get_user_model()


class IndexView(generic.ListView):
    '''Представление главной страницы'''

    template_name = 'polls/index.html'
    context_object_name = 'polls_list'

    def get_queryset(self):
        return Poll.objects.all()


def poll_detail(request, poll_id):
    '''Представление выбранного опроса'''

    context = {
        'poll': Poll.objects.get(id=poll_id),
        'questions': Question.objects.filter(poll_id=poll_id).order_by('id'),
    }
    return render(request, 'polls/poll.html', context)


class QuestionView(generic.DetailView):
    '''Представление каждого вопроса'''

    model = Question
    template_name = 'polls/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def vote(request, question_id):
    '''Представление голосования в опросах'''

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Выберете вариант ответа!',
        })
    if Point.objects.filter(user=request.user, question=question).exists():
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Вы уже голосовали!',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        Point.objects.create(user=request.user, question=question)
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
        )


class ResultsView(generic.DetailView):
    '''Представление результатов ответа'''

    model = Question
    template_name = 'polls/results.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersListView(generic.ListView):
    '''Представление списка пользователей'''

    template_name = 'polls/users.html'
    context_object_name = 'point_list'

    def get_queryset(self):
        return User.objects.all()


class ProfileView(generic.DetailView):
    '''Представление страницы пользователя'''

    model = Point
    template_name = 'polls/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AboutAuthorView(TemplateView):
    '''Представление страницы об авторе'''
    template_name = 'about/author.html'
