from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Imagen
from .forms import ImagenForm
from django.contrib.auth.decorators import login_required

def lista_imagenes(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'lista_imagenes.html', {'imagenes': imagenes})

def detalle_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    return render(request, 'detalle_img.html', {'imagen': imagen,'request':request})

def lista_imagen2(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'lista_img2.html', {'imagenes': imagenes})


def subir_imagen(request):
   # if request.user.perfil.rol in ['editor', 'administrador']:
        if request.method == 'POST':
            form = ImagenForm(request.POST, request.FILES)
            if form.is_valid():
                imagen = form.save(commit=False)
                imagen.autor = request.user
                imagen.save()
                return redirect('galeria:detalle_imagen', pk=imagen.pk)
        else:
            form = ImagenForm()
        return render(request, 'subir_imagen.html', {'form': form})
    #else:
     #   return redirect('galeria:lista_imagenes')


def editar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    #if request.user == imagen.autor or request.user.perfil.rol == 'administrador':
    if request.method == 'POST':
            form = ImagenForm(request.POST, request.FILES, instance=imagen)
            if form.is_valid():
                form.save()
                messages.success(request, 'Imagen actualizada exitosamente.')
                return redirect('galeria:detalle_imagen', pk=imagen.pk)
    else:
            form = ImagenForm(instance=imagen)
    return render(request, 'editar_imagen.html', {'form': form, 'imagen': imagen})
    #else:
       # messages.error(request, 'No tienes permiso para editar esta imagen.')
        #return redirect('galeria:detalle_imagen', pk=pk)
    

def eliminar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    #if request.user == imagen.autor or request.user.perfil.rol == 'administrador':
    if request.method == 'POST':
            imagen.delete()
            messages.success(request, 'Imagen eliminada exitosamente.')
            return redirect('galeria:lista_imagenes')
    else:
            return render(request, 'eliminar_imagen.html', {'imagen': imagen})
    #else:
        #messages.error(request, 'No tienes permiso para eliminar esta imagen.')
        #return redirect('galeria:detalle_imagen', pk=pk)

