from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import WordQuiz

# пример простейшей вьющки
def hello_world(request):
    return HttpResponse("Hello, world!")

# функция для рендера вьюшки корневой страницы
def index(request):
    word_list = WordQuiz.objects.all()
    context = {"word_list":word_list}
    # ренедр шаблона 'templates/index.html'
    return render(request, 'index.html', context)


def word_quiz(request, word_id):
    word_quiz = get_object_or_404(WordQuiz, pk=word_id)
    context = {"word_quiz":word_quiz}
    return render(request, 'word_quiz.html', context)


def check(request, word_id):
    return HttpResponse("id %s." % word_id)