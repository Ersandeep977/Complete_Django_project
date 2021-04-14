from django.shortcuts import render
from E_App.models import Employes


# Create your views here.
def Emp_view(request):
    Emp_list=Employes.objects.all()
    my_dict={'emp_list':Emp_list}
    return render(request,'MyApp/Index.html',context=my_dict)

def Emp_info(request):
    return render(request,'MyApp/Empinfomation.html')
