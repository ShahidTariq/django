from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Classes, Subjects, Fees
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    template = loader.get_template('school/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def classes(request):
    class_list = Classes.objects.all()
    template = loader.get_template('school/classes.html')
    context = {
        'class_list': class_list,
    }
    return HttpResponse(template.render(context, request))


def subjects(request):
    subject_list = Subjects.objects.all()
    class_list = Classes.objects.all()
    template = loader.get_template('school/subjects.html')
    context = {
        'subject_list': subject_list,
        'class_list': class_list,
    }
    return HttpResponse(template.render(context, request))


def fees(request):
    fee_list = Fees.objects.all()
    class_list = Classes.objects.all()
    template = loader.get_template('school/fees.html')
    context = {
        'fee_list': fee_list,
        'class_list': class_list,
    }
    return HttpResponse(template.render(context, request))


def addSubject(request):
    try:
        if request.method == 'POST':
            c = get_object_or_404(Classes, pk=request.POST['classId'])
    except (KeyError, Classes.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'school/subjects.html', {
            'error_message': "Cannot insert subject details.",
        })
    else:
        c.subjects_set.create(subject_name=request.POST['name'], max_marks=request.POST['maxmarks'])

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        context = {}
        template = loader.get_template('school/subjects.html')
        return HttpResponseRedirect("subjects")


def addClass(request):

    try:
        if request.method == 'POST':
            pass

    except (KeyError, Classes.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'school/classes.html', {
            'error_message': "Cannot insert class details.",
        })
    else:
        classRecord=Classes()
        classRecord.class_name = request.POST['name']
        classRecord.class_desc = request.POST['desc']
        classRecord.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        context = {}
        template = loader.get_template('school/classes.html')
        return HttpResponseRedirect("classes")


def addFee(request):
    try:
        if request.method == 'POST':
            f = get_object_or_404(Classes, pk=request.POST['classId'])
    except (KeyError, Classes.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'school/fees.html', {
            'error_message': "Cannot insert subject details.",
        })
    else:
        f.fees_set.create(fee_amount=request.POST['amount'], frequency=request.POST['frequency'])

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        context = {}
        template = loader.get_template('school/fees.html')
        return HttpResponseRedirect("fees")


def deleteClass(request, class_id):

    try:
        selected_choice = get_object_or_404(Classes, id=request.POST['class_id'])

    except (KeyError, Classes.DoesNotExist):

        # Redisplay the question voting form.
        return HttpResponseRedirect("classes")
    else:
        selected_choice.delete()  # line 1

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('school:classes'))


def deleteSubject(request, subject_id):

    try:
        selected_choice = get_object_or_404(Subjects, id=request.POST['subject_id'])

    except (KeyError, Subjects.DoesNotExist):

        # Redisplay the question voting form.
        return HttpResponseRedirect("subjects")
    else:
        selected_choice.delete()  # line 1

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('school:subjects'))

def deleteFee(request, fee_id):

    try:
        selected_choice = get_object_or_404(Fees, id=request.POST['fee_id'])

    except (KeyError, Subjects.DoesNotExist):

        # Redisplay the question voting form.
        return HttpResponseRedirect("fees")
    else:
        selected_choice.delete()  # line 1

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('school:fees'))
