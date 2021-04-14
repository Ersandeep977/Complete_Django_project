from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'MyApp/home.html')

def movie(request):
    return render(request,'MyApp/movies.html')

def sport(request):
    return render(request,'MyApp/sport.html')