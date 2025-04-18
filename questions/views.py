from django.shortcuts import render
from .models import Question_schema

# Create your views here.
def homepage(request):
    question_first = Question_schema.objects.all().first()
    context = {'question': question_first}
    return render(request, 'questions/index.html', context)

def question(request, question_id):
    q = Question_schema.objects.filter(question_num=question_id)[:1].get()
    context = {'question': q}
    return render(request, 'questions/question.html', context)

def error(request):
    return render(request, 'questions/error.html', {})

def result(request, question_id, answer):
    q = Question_schema.objects.filter(question_num=question_id)[:1].get()
    if answer == "yes":
        a = q.yes_answer_text.split("-",1)
    else:
        a = q.no_answer_text.split("-",1)
    a2 = []
    for each in a:
        a2.append(each.strip())
    context = {'answer': a2}
    return render(request, 'questions/result.html', context)

def promo(request):
    return render(request, 'questions/promo.html', {})
