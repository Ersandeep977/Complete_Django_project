from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'MyApp/index.html')

def moviesinfo(request):
    head_masg='Leatest Movies Information '
    msg1 = 'salman khan ki sadi ho rahi he'
    mag2 = 'but yo kar le tab to'
    mag3 = 'ap sab log ko jadi hi bata dege'
    my_dict = {'head_masg': head_masg, 'msg1': msg1, 'mag2': mag2, 'mag3': mag3}
    return render(request,'MyApp/news.html',context=my_dict)

def sportinfo(request):
    head_masg = 'Leatest Sport Information '
    msg1 = 'salman khan ki sadi ho rahi he'
    mag2 = 'but yo kar le tab to'
    mag3 = 'ap sab log ko jadi hi bata dege'
    my_dict = {'head_masg': head_masg, 'msg1':msg1, 'mag2':mag2, 'mag3':mag3}
    return render(request, 'MyApp/news.html', context=my_dict)

def polictsinfo(request):
    head_masg = 'Leatest Policts Information '
    msg1 = 'salman khan ki sadi ho rahi he'
    mag2 = 'but yo kar le tab to'
    mag3 = 'ap sab log ko jadi hi bata dege'
    my_dict = {'head_masg': head_masg, 'msg1': msg1, 'mag2': mag2, 'mag3': mag3}
    return render(request, 'MyApp/news.html', context=my_dict)