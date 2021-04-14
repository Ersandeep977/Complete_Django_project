import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelInhri_pro.settings')
import django
django.setup()

from app.models import *
from faker import Faker
from random import *
faker = Faker('en_IN')

def phonenumberGen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populater(n):
    for i in range(n):
        fEid=faker.random_int(100,999)
        print(fEid)
        fEname=faker.name()
        print(fEname)
        fEsal=faker.random_int(10000,20000)
        print(fEsal)
        fEaddress=faker.address()
        print(fEaddress)
        fEemail=faker.email()
        print(fEemail)
        fphonenumber=phonenumberGen()
        print(fphonenumber)
        Employes_recode=Employes.objects.get_or_create(Eid=fEid,
                                                       EName=fEname,
                                                       ESal=fEsal,
                                                       Eaddress=fEaddress,
                                                       Eemail=fEemail,
                                                       phoneno=fphonenumber)
populater(10)
print("Data Secssefull Populate NoW you Can Check..DATABASE")
print('YOU CAN USE " PY.MANAGE.PY RUNSERVER "')


