from django.shortcuts import render
from django.http import HttpResponse

# пример простейшей вьющки
def hello_world(request):
    return HttpResponse("Hello, world!")

# функция для рендера вьюшки корневой страницы
def index(request):
    context = {"latest_question_list":not True}
    # ренедр шаблона 'templates/index.html'
    return render(request, 'index.html', context)