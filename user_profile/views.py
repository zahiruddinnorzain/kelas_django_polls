from django.shortcuts import render, redirect
from register.models import Register

def index(request):
    user = Register.objects.filter(ic_text='123').first() #123 tu ganti dengan session
    '''
    user_ic = user.ic_text
    user_sex = user.sex
    user_monthly_salary_text = user.monthly_salary_text
    '''
    context = {
        'posts': user,
    }
    return render(request, 'undi/profile.html', context)