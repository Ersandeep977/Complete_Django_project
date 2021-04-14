import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUD_project.settings')
import django
django.setup()

from app.models import *
from faker import Faker
from random import *
faker=Faker()

def phonenumberGen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populater(n):
    for i in range(n):
        feno=randint(1001,9999)
        fname=faker.name()
        fesal=randint(10000,30000)
        feadd=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fname,esal=fesal,eadd=feadd)
    print(" Populating Processing...OK")

populater(5)
print("Data Secssefull Populate NoW you Can Check..DATABASE..'OK'")
print('YOU CAN USE " PY.MANAGE.PY RUNSERVER "')


