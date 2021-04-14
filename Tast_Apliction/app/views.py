from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    msg='Hello Guest!!! very Very Good '
    h=int(date.strftime('%H'))
    if h<12:
        msg='Morning!!!'
    elif h<16:
        msg='After Noon!!!'
    elif h<21:
        msg='Eving!!!'
    else:
        msg='Hello Guest!!! Very Very Good Night !!!'
        my_dict={'insert_date':date,'insert_msg':msg}
        return  render(request,'MyApp/home.html',my_dict)
