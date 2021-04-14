from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.forms import SigUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'MyApp/home.html')

@login_required()
def java_page_view(request):
    return render(request,'MyApp/JavaExam.html')

@login_required()
def python_page_view(request):
    return render(request,'MyApp/Python.html')

def logout_page(request):
    return render(request,'MyApp/logout.html')

def SigUp_view(request):
    form = SigUpForm()
    if request.method == 'POST':
        form = SigUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'MyApp/SigUp.html',{'form':form})