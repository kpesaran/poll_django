from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    loader.get_template("polls/index.html")
    context = {"latest_question_list":latest_question_list, }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")

def example(request, question_id):
    return HttpResponse(f"Look at the url, you will see {question_id}")



