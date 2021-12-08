from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import car

class Car_Listview(ListView):
    template = 'car_list.html'
    model = car

class Car_Detailview (DetailView):
    template = 'car_detail.html'
    model = car

class Car_Createview(CreateView):
    template = 'car_create.html'
    model = car
    fields = ['name', 'price', 'image']
    success_url = reverse_lazy('car_list')

class Car_Updateview(UpdateView):
    template = 'car_update.html'
    model = car
    fields = ['name', 'price', 'image']

class Car_deleteview(DeleteView):
    template = 'car_delete.html'
    model = car
    success_url = reverse_lazy('car_list')
    