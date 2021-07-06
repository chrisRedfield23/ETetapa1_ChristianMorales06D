from django.shortcuts import render, redirect
from .models import colaboradores
from .forms import colaboForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def ver(request):
    col = colaboradores.objects.all()
    return render(request, 'ver.html', context={'usuarios':col}) 

def creaar(request):
    if request.method=='POST':
         colab_form = colaboForm(request.POST, request.FILES)
         if colab_form.is_valid():
             colab_form.save()
             return redirect('ver')
    else:
        colab_form = colaboForm()    
    return render(request, 'creaar.html', {'colab_form':colab_form})

def eliminar(request,id):
    usuario = colaboradores.objects.get(rut=id)
    usuario.delete()
    return redirect('ver')

def modificar(request,id):
    usuario = colaboradores.objects.get(rut=id)

    datos ={
        'form': colaboForm(instance=usuario)
    }
    if request.method == 'POST': 
        formulario = colaboForm(data=request.POST, instance = usuario)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'modificar.html', datos)


