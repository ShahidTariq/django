from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Index</h1>, Welcome to school.")


def classes(request):
    return HttpResponse("<h1>Classes</h1>, Welcome to school.")


def subjects(request):
    return HttpResponse("<h1>Subjects</h1>, Welcome to school.")


def fees(request):
    return HttpResponse("<h1>Fees</h1>, Welcome to school.")