from django.shortcuts import render,redirect
from app.models import Employee
from app.forms import EmployesForm

# Create your views here.
def retrieve_view(request):
    employes=Employee.objects.all()
    return render(request,'MyApp/index.html',{'empolyes':employes})

def create_view(request):
    form=EmployesForm()
    if request.method=='POST':
        form=EmployesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render(request,'MyApp/create.html',{'form':form})

def delete_view(request,id):
    employes=Employee.objects.get(id=id)
    employes.delete()
    return redirect('/home')

def Udate_view(request,id):
    employes=Employee.objects.get(id=id)
    if request.method == 'POST':
        form=EmployesForm(request.POST,instance=employes)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request,'MyApp/Udate.html',{'employes':employes})

