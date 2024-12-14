from django.db import models

# классы моделей (абстрактны структуры данных)

# класс бля изучения языка
class WordQuiz(models.Model):
    # поле индекса нужно для сохранения прогресса
    id = models.AutoField(primary_key=True, help_text='поле индекса нужно для сохранения прогресса')
    # поле слова (каждое поле уникально)
    word = models.CharField(max_length=50, unique=True, help_text='слово изучаемого языка')
    # перевод (для разных слов может повторяться)
    translation = models.CharField(max_length=50, help_text='перевод слова')



