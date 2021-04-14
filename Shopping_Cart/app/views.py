from django.shortcuts import render
from app.forms import AddItemForm

# Create your views here.
def Add_item_view(request):
    form=AddItemForm()
    if request.method == 'POST':
        Name = request.POST['name']
        quantity=request.POST['quantity']
        request.session['Name']=Name
    return render(request,'MyApp/additem.html',{'form':form})

def display_item_view(request):
    return render(request,'MyApp/displayItems.html')