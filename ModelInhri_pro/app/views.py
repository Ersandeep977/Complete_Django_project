from django.shortcuts import render
from app.models import Employes
import datetime

# Create your views here.
def Home_view(request):
    date=datetime.datetime.now()
    Emp=Employes.objects.all()
    count=Emp.count()
    my_Dict={'date':date,'Count':count,'Emp':Emp}
    return render(request,'MyApp/home.html',context=my_Dict)