from django.contrib import admin
from .models import WordQuiz

# регистрируем классы моделей бля работы с ними в админки

admin.site.register(WordQuiz)
