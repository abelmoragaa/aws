from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Perfil#Importamos el modelo Perfil de la app usuarios


@receiver(post_save, sender=User)

def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:#Si se cread un usuario
        Perfil.objects.create(user=instance)

#Función para guardar
@receiver(post_save, sender=User)#
def guardar_perfil_usuario(sender, instance, **kwargs):#recibe la señal post_save
    instance.perfil.save()#Guardar