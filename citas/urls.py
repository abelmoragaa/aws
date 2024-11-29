from django.urls import path
from . import views

app_name = 'citas'

urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('cita/<int:pk>/', views.detalle_cita, name='detalle_cita'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('vista_panel/', views.vista_panel, name='vista_panel'),
    path('lista2', views.lista_citas2, name='lista_citas2'),
    
]
