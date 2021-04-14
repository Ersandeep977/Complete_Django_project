from django.shortcuts import render
from app.forms import NameForm,AgrForm,GfForm

# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,'MyApp/Name.html',{'form':form})

def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgrForm()
    return render(request,'MyApp/Age.html',{'form':form})

def Gf_view(request):
    age = request.GET['age']
    request.session['age'] = age
    form = GfForm()
    return render(request,'MyApp/Gfname.html',{'form':form})

def resut_view(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    return render(request,'MyApp/Resut.html')