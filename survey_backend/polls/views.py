from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .models import Question, Choice


class IndexView(generic.ListView):
    '''Представление главной страницы'''

    template_name = 'polls/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    '''Представление вопроса'''

    model = Question
    template_name = 'polls/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ResultsView(generic.DetailView):
    '''Представление результатов ответа'''

    model = Question
    template_name = 'polls/results.html'

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
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
        )


class AboutAuthorView(TemplateView):
    '''Представление страницы об авторе'''
    template_name = 'about/author.html'
