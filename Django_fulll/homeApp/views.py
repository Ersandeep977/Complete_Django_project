from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={'varibale':'this send data'}
    return render(request,'Indext.html',context)
def about(request):
    #return HttpResponse('<h1>this is about page</h1>')
    return render(request,'about.html')
def services(request):
    #return HttpResponse('<h1>this is Services page</h1>')
    return render(request,'services.html')
def contact(request):
    #return HttpResponse('<h1>this is contact page</h1>')
    return render(request,'contact.html')