from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is tech home page</h1>")