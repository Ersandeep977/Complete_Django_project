from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    print('this line printing by view function while proessing request')
    return HttpResponse('<h1>Custom middleare Demo</h1>')

def show(request):
    return render(request,'MyApp/home.html')