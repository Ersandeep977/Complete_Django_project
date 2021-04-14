from django.shortcuts import render

# Create your views here.
def count_view(request):
    if'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'MyApp/Count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return response
