from dataclasses import fields
import profile
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from requests import post
from django.views.generic.detail import SingleObjectMixin
from petmatchaut.models import pet_perfil
from petmatchaut.forms import petPerfilForm
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.contrib.auth.models import User

def insert(request):
    form = petPerfilForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request,'home.html')

def form(request):
    data = {}
    data['form'] = petPerfilForm()
    return render(request, 'form.html', data)       

def saveData(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = pet_perfil.objects.filter(nome__icontains=search)
    else:
        data['db'] = pet_perfil.objects.all()

    return render(request, 'home.html', data)
   
class Profile(ListView):
    model = pet_perfil
    template_name = 'account/profile.html'



class addPet(CreateView):
    model = pet_perfil
    form_class = petPerfilForm
    template_name = 'account/add_pet.html'
    success_url = reverse_lazy('profile')



class HomeView(TemplateView):
    template_name = 'home.html'

    
