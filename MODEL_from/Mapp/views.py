from django.shortcuts import render
from Mapp import forms
from django.http import HttpResponseRedirect

# Create your views here.
def EmpData(request):
    if request.method=="POST":
        form =forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.EmpForm()
    return render(request,'MyApp/empdata.html',{'form':form})


def Thanks(request):
    return render(request,'MyApp/thanks.html')
