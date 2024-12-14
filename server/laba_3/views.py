from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import WordQuiz

COOKIE_NAME = "quiz_last"


# пример простейшей вьющки
def hello_world(request):
    return HttpResponse("Hello, world!")


# функция для рендера вьюшки корневой страницы
def index(request):
    word_list = WordQuiz.objects.all()
    context = {"word_list": word_list}
    # ренедр шаблона 'templates/index.html'
    return render(request, "index.html", context)


def word_quiz(request, word_id):
    cookie_value = request.COOKIES.get(COOKIE_NAME, "default_value")
    word_quiz = get_object_or_404(WordQuiz, pk=word_id)
    context = {"word_quiz": word_quiz, "cookie_value": cookie_value}
    return render(request, "word_quiz.html", context)


def check(request, word_id):
    response = HttpResponse(f"id {word_id} {type(word_id).__name__}")
    last_index = 0
    try:
        cookie_string = request.COOKIES.get(COOKIE_NAME, "0")
        last_index = int(cookie_string)
    except ValueError:
        last_index = 0
    if word_id > last_index:
        response.set_cookie(COOKIE_NAME, word_id)
    return response


def get_cookie_view(request):
    # TODO
    cookie_value = request.COOKIES.get(COOKIE_NAME, "default_value")
    return HttpResponse(f"The value of my_cookie is {cookie_value}")
