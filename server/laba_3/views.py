from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def hello_world(request):
    return HttpResponse("Hello, world. You're at the index.")

def index(request):
    # template = loader.get_template("index.html")
    context = {}
    # return HttpResponse(template.render(context, request))
    return HttpResponse("Hello, world. Laba 3")