from django.shortcuts import render
from J_App.models import *
import datetime

# Create your views here.
def index(request):
    date=datetime.datetime.now()
    name='sandeep'
    my_dict={'date':date,'name':name}
    return render(request,'MyApp/Index.html',context=my_dict)

def Hyd_job_info(request):
    Jobs_lists=Hyd_jobs.objects.all()
    my_dict={'job_list':Jobs_lists}
    return render(request,'MyApp/HydJob.html',context=my_dict)

def Pune_job_info(request):
    Jobs_list=Pune_jobs.objects.order_by('date')
    my_dict={'job_list':Jobs_list}
    return render(request,'MyApp/PuneJob.html',context=my_dict)

def Chani_job_info(request):
    Jobs_list=Chann_jobs.objects.all()
    my_dict={'job_list':Jobs_list}
    return render(request,'MyApp/ChanJob.html',context=my_dict)
