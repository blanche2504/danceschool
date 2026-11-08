from django.shortcuts import render

__all__ = [
    "about",
    "home",
]


def home(request):
    return render(request, template_name="home.html")


def about(request):
    return render(
        request,
        template_name="about.html",
    )
