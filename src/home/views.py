from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

PROJECT_NAME = getattr(settings, "PROJECT_NAME", "Unset project in views.py")


def hello_world(request):
    return render(request, "hello-world.html", {
        "project_name": PROJECT_NAME,
    })


def health_check(request):
    return HttpResponse("OK", status=200)
