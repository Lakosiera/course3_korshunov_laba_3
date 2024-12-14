from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
    last_index = get_cookie_int(request, COOKIE_NAME, 1)
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
    # запросить из бызы обьект с идентификатором word_id, в случае нейдачи вывести старницу 404
    word_quiz = get_object_or_404(WordQuiz, pk=word_id)

    # достаем из формы запроса поле "translation"
    if word_quiz.translation == request.POST["translation"]:
        # если перевод совпадает
        # устанавливаем переменную для id следующего слова
        next_id = word_id + 1
        # запрашиваем из базы последее слово и получаем его id
        last_id = WordQuiz.objects.last().id

        # если следующего id нет в базе данных
        if next_id > last_id:
            # создаем сообщение об успехе
            messages.success(request, "Вы все прошли!")
            # перенаправляем на главную страницу
            return HttpResponseRedirect(
                # создаем редирект
                reverse(
                    # имя редиреакта из "urls.py"
                    "index"
                )
            )

        # создаем запрос с перенаправление на страницу перевода с параметром id следующего слова
        response = HttpResponseRedirect(
            # создаем редирект
            reverse(
                # имя редиреакта из "urls.py"
                "quiz",
                # передаем аргументы в запрос
                args=(next_id,),
            )
        )
        # в запросе указываем что записываем cookie
        response.set_cookie(COOKIE_NAME, next_id)
        # возвращаем запрос / выполняем запрос / выводим страницу
        return response
    else:
        # если перевод не совпадает
        # создаем сообщение с ошибкой
        messages.error(request, "Неправиьно!")
        # создаем запрос с перенаправлением на страницу перевода с параметром id текущего слова
        return HttpResponseRedirect(
            # создаем редирект
            reverse(
                # имя редиреакта из "urls.py"
                "quiz",
                # передаем аргументы в запрос
                args=(word_id,),
            )
        )


# функция для сброса cookie
def reset(request):
    # создаем отвт редиректа на главную страницу
    response = HttpResponseRedirect(reverse("index"))
    # передаем сообщение
    messages.info(request, "Сookie удален")
    # удалаяем cookie
    response.delete_cookie(COOKIE_NAME)
    # возвращаем ответ / выводим страницу
    return response


# утилитарная функция для получения cookie как целое число
def get_cookie_int(request, key, default=0):
    try:
        # получение cookie
        cookie_string = request.COOKIES.get(key, default)
        # преобразование строки в целое число
        return int(cookie_string)
    except ValueError:
        # в случаеш ошибки возврщаем значение по умолчанию
        return default
