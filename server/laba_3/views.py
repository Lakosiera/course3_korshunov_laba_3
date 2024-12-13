from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, world. You're at the index.")

def index(request):
    context = {"latest_question_list":not True}
    return render(request, "index.html", context)