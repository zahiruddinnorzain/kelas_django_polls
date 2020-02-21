from django import forms
from .models import Register
from django.forms import ModelForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["name_text", "ic_text", "sex", "monthly_salary_text"]
