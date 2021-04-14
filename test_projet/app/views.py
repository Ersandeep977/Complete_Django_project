from django.shortcuts import render
from app.models import Company
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView

# Create your views here.
class CompnyListView(ListView):
    model = Company


class CompnyDetailView(DetailView):
    model = Company

class companyCreate(CreateView):
    model = Company
    fields = "__all__"


