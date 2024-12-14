from django.contrib import admin
from .models import WordQuiz


# класс обвертка над 'WordQuiz' для работы в админке
class WordQuizAdmin(admin.ModelAdmin):
    # отображаем поля обьекта в админке
    list_display = ('id', 'word', 'translation')


# регистрируем классы моделей бля работы с ними в админке
admin.site.register(WordQuiz, WordQuizAdmin)
