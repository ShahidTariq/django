from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    template = loader.get_template('ajaxApp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
