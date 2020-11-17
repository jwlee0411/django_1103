from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from django.template import loader

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("Hello, world. You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("Hello, world. You're looking at results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("Hello, world. You're voting on question %s." % question_id)
