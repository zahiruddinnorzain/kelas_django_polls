from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
           latest_question_list = Question.objects.order_by('-pub_date')[:5]
           template = loader.get_template('undi/index.html')
           context = {
                     'latest_question_list':latest_question_list,
           }
           return render(request, 'undi/index.html', context)
           #return HttpResponse(template.render(context, request))

#def index(request):
 #         latest_question_list = Question.objects.order_by('-pub_date')[:5]
 #         output = ', '.join([q.question_text for q in latest_question_list])
 #         return HttpResponse(output)

#def index2(request):
 #         return HttpResponse("hoi hello sini tempat undi weh!")

def detail(request, question_id):
          return HttpResponse("you are looking at question %s." % question_id)

def results(request, question_id):
          response = "you are looking at the same result of question %s."
          return HttpResponse(response % question_id)

def vote(request, question_id):
          return HttpResponse("You're voting on question %s." % question_id)

def question_view(request):
          question = Question.objects.all()
          context = {
                    'question' : question
          }

          return render(request, 'undi/questions.html', context)