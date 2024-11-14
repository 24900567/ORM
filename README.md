# Ex02 Django ORM Web Application
## Date: 14.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<WhatsApp Image 2024-11-14 at 14.28.48_a6dbc3b6.jpg>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Bankloan,Bankloanadmin
admin.site.register(Bankloan,Bankloanadmin)


models.py

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

```



## OUTPUT
![alt text](<Screenshot 2024-11-14 141649.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
