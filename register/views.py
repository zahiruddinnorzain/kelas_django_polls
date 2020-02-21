from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse



'''
def get_register(request):
    # if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = RegisterForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
			
			name_text = form.cleaned_data['name_text']
			ic_text = form.cleaned_data['ic_text']
			sex = form.cleaned_data['sex']
			monthly_salary_text = form.cleaned_data['monthly_salary_text']

			form.save()
			#print("sukses")

		return HttpResponse('tq')
	else:
		form = RegisterForm()

	return render(request, 'undi/register.html', {'form': form})
'''

def get_register(request):
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = RegisterForm()
	
	context = {'form':form}
	return render(request, 'undi/register.html', context)
