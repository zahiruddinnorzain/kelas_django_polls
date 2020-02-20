from django.urls import path
from . import views

urlpatterns = [
          #path('', views.index, name='index'),
          path('question/', views.question_view, name='question_view'),
          # ex: /polls/
          path('', views.index, name='index'),
          # ex: /polls/5/
          path('<int:question_id>/', views.detail, name='detail'),
          # ex: /polls/5/results/
          path('<int:question_id>/results/', views.results, name='results'),
          # ex: /polls/5/vote/
          path('<int:question_id>/vote/', views.vote, name='vote'),


]