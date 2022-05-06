from django.shortcuts import redirect, render
from petmatchaut.models import pet_perfil
from petmatchaut.forms import petPerfilForm

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

