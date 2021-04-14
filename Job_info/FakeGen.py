import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Job_info.settings')
import django
django.setup()

from J_App.models import *
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
        fdate=faker.date()
        fcompany=faker.company()
        ftitle=faker.random_element(elements=('projectManager','Tester','Team leader','softwerEng'))
        felibility=faker.random_element(elements=('B.Tech','M.Tech','BBA','BCA','MCA'))
        faddress=faker.address()
        femail=faker.email()
        fphonenumber=phonenumberGen()
        Hydjobs_recode=Hyd_jobs.objects.get_or_create(date=fdate,company=fcompany,
                                                      title=ftitle,
                                                      elisbility=felibility,
                                                      address=faddress,
                                                      email=femail,
                                                      phoneno=fphonenumber)
        print("'HYDJOB'Data Populating Processing...OK")
        Punejobs_recode = Pune_jobs.objects.get_or_create(date=fdate,
                                                        company=fcompany,
                                                        title=ftitle,
                                                        elisbility=felibility,
                                                        address=faddress,
                                                        email=femail,
                                                        phoneno=fphonenumber)
        print("'PUNEJOB'Data Populating Processing...OK")
        Channjobs_recode = Chann_jobs.objects.get_or_create(date=fdate,
                                                        company=fcompany,
                                                        title=ftitle,
                                                        elisbility=felibility,
                                                        address=faddress,
                                                        email=femail,
                                                        phoneno=fphonenumber)
        print("'CHANNIEJOB'Data Populating Processing...OK")
populater(100)
print("Data Secssefull Populate NoW you Can Check..DATABASE")
print('YOU CAN USE " PY.MANAGE.PY RUNSERVER "')


