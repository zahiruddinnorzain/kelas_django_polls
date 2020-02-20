from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
          return HttpResponse("hoi hello sini tempat undi weh!")

def question_view(request):
          question = Question.objects.all()
          context = {
                    'question' : question
          }

          return render(request, 'undi/questions.html', context)