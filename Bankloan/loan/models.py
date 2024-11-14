from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    Customer_id=models.IntegerField(primary_key=True)
    Customer_name=models.CharField(max_length=100)
    salary=models.IntegerField()
    Customer_age=models.IntegerField()
    Loan_Amount=models.IntegerField()
 
class Bankloanadmin(admin.ModelAdmin):
    list_display=('Customer_id','Customer_name','salary','Customer_age','Loan_Amount')



# Create your models here.
