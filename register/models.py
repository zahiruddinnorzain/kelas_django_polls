from django.db import models

class Register(models.Model):
    name_text = models.CharField(verbose_name='Nama Penuh', max_length=200)
    ic_text = models.CharField('Kad Pengenalan', max_length=14)
    sex = models.BooleanField('Jantina')
    monthly_salary_text = models.IntegerField('Pendapatan Sebulan')
          
    #pub_date = models.DateTimeField('date published')
    def __str__ (self):
        return self.name_text
