from django.shortcuts import render
from app.forms import MovieForm
from app.models import Movies
# Create your views here.

def index_view(request):
    return render(request,'MyApp/index.html')

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'MyApp/addmovie.html',{'form':form})

def list_movie_view(request):
    movies_list=Movies.objects.all().order_by('-rating')
    return render(request,'MyApp/listmovie.html',{'movies_list':movies_list})