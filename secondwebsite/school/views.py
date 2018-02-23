from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import Classes, Subjects, Fees
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
def index(request):
    template = loader.get_template('school/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url="/school/login/")
def classes(request):
    class_list = Classes.objects.all()

    if request.is_ajax():
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

        tableContent=""

        for c in class_list:
            tableContent += "<tr> <td>" + c.class_name + "</td> <td>" + c.class_desc + " </td>  <td> <form action = '" + str(c.id) +"/deleteClass' method = post  ><input type = 'hidden' value = '" + str(c.id) + "' name='class_id' /> <input class ='btn btn-primary' type='submit' value='Delete'> </ form> </ td> </ tr>"

        return HttpResponse(tableContent)

    template = loader.get_template('school/classes.html')

    context = {
        'class_list': class_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/school/login/")
def subjects(request):
    subject_list = Subjects.objects.all()
    class_list = Classes.objects.all()
    template = loader.get_template('school/subjects.html')
    context = {
        'subject_list': subject_list,
        'class_list': class_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/school/login/")
def fees(request):
    fee_list = Fees.objects.all()
    class_list = Classes.objects.all()
    template = loader.get_template('school/fees.html')
    context = {
        'fee_list': fee_list,
        'class_list': class_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/school/login/")
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

@login_required(login_url="/school/login/")
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

        if request.is_ajax():
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            return JsonResponse(model_to_dict(classRecord))

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        context = {}
        template = loader.get_template('school/classes.html')
        return HttpResponseRedirect("classes")

@login_required(login_url="/school/login/")
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

@login_required(login_url="/school/login/")
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

@login_required(login_url="/school/login/")
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

@login_required(login_url="/school/login/")
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


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponseRedirect(reverse('school:index'))