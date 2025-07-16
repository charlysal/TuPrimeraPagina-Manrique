from django.shortcuts import render

def about_me(request):
    return render(request, 'AppCoder/aboutme.html')
from django.shortcuts import render
from ..forms import OperarioFormulario, ClientesFormulario, UnidadesFormulario
from django.shortcuts import render, redirect
from django.shortcuts import render
from ..models import Clientes, Unidades
from django.http import HttpResponse
from django.db.models import Q 

def inicio(request):
    return render(request, "AppCoder/index.html")

def operario(request):
    return render(request, "AppCoder/operario.html")

def clientes(request):
    return render(request, "AppCoder/clientes.html")

def unidades(request):
    return render(request, "AppCoder/unidades.html")


def form_operario(request):
    if request.method == 'POST':
        form = OperarioFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = OperarioFormulario()
    return render(request, 'AppCoder/formularios/form_operario.html', {'form': form})

#def form_clientes(request):
   # if request.method == 'POST':
    #    form = ClientesFormulario(request.POST)
     #   if form.is_valid():
      #      form.save()
       #     return redirect('inicio')
   # else:
    #    form = ClientesFormulario()
  #  return render(request, 'AppCoder/formularios/form_clientes.html', {'form': form})

def form_unidades(request):
    if request.method == 'POST':
        form = UnidadesFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UnidadesFormulario()
    return render(request, 'AppCoder/formularios/form_unidades.html', {'form': form})



def buscar_clientes(request):
    termino = request.GET.get("nombre", "").strip()
    
    if termino:
        # Buscar en nombre, apellido o nombre completo
        from django.db.models import Q
        resultados = Clientes.objects.filter(
            Q(nombre__icontains=termino) | 
            Q(apellido__icontains=termino) |
            Q(nombre__icontains=termino.split()[0]) if len(termino.split()) > 1 else Q()
        )
        
        
        if ' ' in termino:
            partes = termino.split()
            if len(partes) >= 2:
                nombre_parte = partes[0]
                apellido_parte = ' '.join(partes[1:])
                resultados = resultados | Clientes.objects.filter(
                    nombre__icontains=nombre_parte,
                    apellido__icontains=apellido_parte
                )
        
        return render(request, "AppCoder/resultados_busqueda.html", {
            "clientes": resultados,
            "termino_busqueda": termino
        })
    else:
        return render(request, "AppCoder/formularios/buscar_clientes.html")
    
def buscar_unidades(request):
    termino = request.GET.get("termino", "").strip()
    
    if termino:
        from django.db.models import Q
        
        resultados = Unidades.objects.filter(
            Q(modelo__icontains=termino) |
            Q(chasis__icontains=termino) |
            Q(accesorios__icontains=termino)  
        )
        
        return render(request, 'AppCoder/resultados_busqueda_unidades.html', {
            'unidades': resultados,
            'termino_busqueda': termino
        })
    else:
        return render(request, 'AppCoder/formularios/buscar_unidades.html')