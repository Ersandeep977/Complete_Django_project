from django.shortcuts import render
from app.models import Student,Teacher
#from django.db.models import Avg,Sum,Max,Min,Count
import datetime

# Create your views here.
def Student_Vews(request):
    date=datetime.datetime.now()
    STD=Student.objects.all()
    count=STD.count()
    my_dict={'date':date,'std':STD,'count':count}
    return render(request,'MyApp/Student.html',context=my_dict)

def teacher_Vews(request):
    date=datetime.datetime.now()
    Tec=Teacher.objects.all()
    count=Tec.count()
    my_dict={'date':date,'std':Tec,'count':count}
    return render(request,'MyApp/Teacher.html',context=my_dict)

def Total_view(request):
    date=datetime.datetime.now()
    Std=Student.objects.all()
    SCount=Std.count()
    Tec=Teacher.objects.all()
    TCount=Tec.count()

    my_dict={'Std':Std,'Tec':Tec,'date':date,'SCount':SCount,'TCount':TCount}
    return render(request,'MyApp/Total.html',context=my_dict)

