from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min,Count
from app.models import Employes
from django.db.models.functions import Lower
import datetime

# Create your views here.
def disply_View(request):
    employes = Employes.objects.all().order_by(Lower('EName'))
    count=employes.count()
    date=datetime.datetime.now()
    my_dict={'employes':employes,'count':count,'date':date}
    return render(request,'MyApp/indext.html',my_dict)


def Disply_ifo(request):
    avg1=Employes.objects.all().aggregate(Avg('ESal'))
    max=Employes.objects.all().aggregate(Max('ESal'))
    min = Employes.objects.all().aggregate(Min('ESal'))
    sum = Employes.objects.all().aggregate(Sum('ESal'))
    count=Employes.objects.all().aggregate(Count('ESal'))
    my_dict={'avg':avg1,'max':max,'min':min,'sum':sum,'count':count}
    return render(request,'MyApp/Display.html',my_dict)