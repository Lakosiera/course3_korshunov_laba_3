from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import WordQuiz

# константа с именем cookie
COOKIE_NAME = "quiz_last"


# пример простейшей вьющки
def hello_world(request):
    # простейший вывод html страницы
    return HttpResponse("Hello, world!")


# функция для рендера вьюшки корневой страницы
def index(request):
    # запрашиваем из базы все поля таблицы WordQuiz
    word_list = WordQuiz.objects.all()
    # получаем id последнего переведенного слова из cookie брайзера
    last_index = get_cookie_int(request, COOKIE_NAME)
    # создаем словарь контекса чтобы передать переменные в шаблон
    context = {
        # все запрошенные слова
        "word_list": word_list,
        # последний индекс
        "last_index": last_index,
    }
    # ренедр вьюшки в html страницу
    return render(
        # запрос самой вьюшки
        request, 
        # имя шаблона
        template_name="index.html",
        # контекст с переменными
        context=context,
    )


# функция для рендера вьюшки перевода слова
def word_quiz(request, word_id):
    # запросить из бызы обьект с идентификатором word_id, в случае нейдачи вывести старницу 404
    word_quiz = get_object_or_404(WordQuiz, pk=word_id)
    # получаем id последнего переведенного слова из cookie брайзера
    last_index = get_cookie_int(request, COOKIE_NAME)
    # создаем словарь контекса чтобы передать переменные в шаблон
    context = {
        # данные слова из таблицы 
        "word_quiz": word_quiz,
        # последний индекс
        "last_index": last_index,
    }
    # ренедр вьюшки в html страницу
    return render(request, "word_quiz.html", context)


# функция для валидации формы
def check(request, word_id):
    last_index = get_cookie_int(request, COOKIE_NAME)
    response = HttpResponse(f"id= {word_id} last= {last_index}")

    if word_id >= last_index:
        response.set_cookie(COOKIE_NAME, word_id + 1)
    return response


def reset(request):
    response = HttpResponse("Cookie удален!")
    response.delete_cookie(COOKIE_NAME)
    return response


def get_cookie_int(request, key, default=0):
    try:
        cookie_string = request.COOKIES.get(key, default)
        return int(cookie_string)
    except ValueError:
        return default
