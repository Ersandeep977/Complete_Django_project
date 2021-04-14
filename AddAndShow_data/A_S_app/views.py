from django.shortcuts import render
from A_S_app.forms import MoviesForm
from A_S_app.models import Movies
import datetime

# Create your views here.
def Index_view(request):
    date=datetime.datetime.now()
    my_dict={'date':date}
    return render(request,'MyApp/Index.html',context=my_dict)


def Add_movies_view(request):
    form=MoviesForm()
    if request.method=='POST':
        form=MoviesForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return Index_view(request)
    return render(request,'MyApp/AddMovies.html',{'form':form})

def Movies_list(request):
    movies_list=Movies.objects.all()
    return render(request,'MyApp/ShowMList.html',{'Movies_list':movies_list})