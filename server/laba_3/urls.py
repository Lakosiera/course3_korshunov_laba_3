from django.urls import path

from . import views

# пути для модуля 'laba_3'
urlpatterns = [
    # корневой путь (т.е. "/" или "http://localhost:8080/")
    path(
        route="",           # путь
        view=views.index,   # вьюшка из файла 'views.py'
        name="index",       # условное имя пути (можно неуказывать)
    ),
]
