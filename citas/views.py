from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .forms import CitaForm
from django.contrib.auth.decorators import login_required

def lista_citas(request):
    citas = Cita.objects.all().order_by('-fecha')
    return render(request, 'lista.html', {'citas': citas})

def detalle_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, 'detalle.html', {'cita': cita})

def lista_citas2(request):
    citas = Cita.objects.all().order_by('-fecha')
    return render(request, 'lista2.html', {'citas': citas})

@login_required
def crear_cita(request):
    #if request.user.perfil.rol in ['editor', 'administrador']:
        if request.method == 'POST':
            form = CitaForm(request.POST)
            if form.is_valid():
                cita = form.save(commit=False)
                cita.autor = request.user
                cita.save()
                return redirect('citas:lista_citas', )
        else:
            form = CitaForm()
        return render(request, 'crear.html', {'form': form})
    #else:
        #return redirect('citas:lista_citas')

@login_required
def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
   #if request.user == cita.autor or request.user.perfil.rol == 'administrador':
    if request.method == 'POST':
            form = CitaForm(request.POST, instance=cita)
            if form.is_valid():
                form.save()
                return redirect('citas:detalle_cita', pk=cita.pk)
    else:
            form = CitaForm(instance=cita)
    return render(request, 'editar.html', {'form': form})
   # else:
   #     return redirect('citas:lista_citas')


def vista_panel(request):
    # Aquí puedes pasar opciones personalizadas basadas en el rol del usuario
    return render(request, 'vista_panel.html')  # Nombre del template que vamos a crear