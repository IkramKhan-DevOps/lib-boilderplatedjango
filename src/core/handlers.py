from django.shortcuts import render


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")