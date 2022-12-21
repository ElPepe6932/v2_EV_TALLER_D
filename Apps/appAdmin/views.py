from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Apps.loginApp.models import User, Reserva
from .forms import *
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponse
from .utils import render_to_pdf
from Apps.sReservas.forms import *
from django.contrib import messages
from Apps.loginApp.forms import *
# pip freeze > requirements. txt  --------> Funciona para desplegar mas facil

# LIBRERIAS

# pip install xhtml2pdf ----> para los reportes

# Create your views here.

# nombre y contraseña superuser MatiasZ 21204650

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def funcionesAdmin(request):
    return render(request, 'panelAdmin.html')

@login_required
def adminEstacionamiento(request):
    return render(request, 'adminEstacinamiento.html')

@login_required
def generarReportes(request):
    return render(request, 'generarReportes.html')

@login_required
def verUsers(request, user_id):
    users = User.objects.get(id=user_id)
    return render(request, 'mostrarUsers.html',{'usuario':users})

#-----------------------------------------------------------------------
@login_required
def vetarUsuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    if usuario.estado == True:
        usuario.estado = False
        usuario.save()
    # return render(request, 'buscarUsuariosAdmin.html',{'alert':f'se a betado al usuario : {self} '})
    return redirect('buscador')

#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
@login_required
def anularVetarUsuario(request, user_id):
    usuario = User.objects.get(id=user_id)
    if usuario.estado == False:
        usuario.estado = True
        usuario.save()
    # return render(request, 'buscarUsuariosAdmin.html',{'alert':f'se a betado al usuario : {self} '})
    return redirect('buscador')
#-----------------------------------------------------------------------


@login_required
def buscarUsuariosAdmin(request):
    busqueda = request.GET.get('buscado')
    usuariosList = User.objects.all()
    if busqueda:
        usuariosList = User.objects.filter(username__icontains = busqueda) 
     
    return render(request, 'buscarUsuariosAdmin.html',{'usuarios':usuariosList})

@login_required
def crearEstacionamiento(request):
    if request.method == 'POST':
        formEstacionamiento = EstacionamientoForm(request.POST)
        if formEstacionamiento.is_valid():
                formEstacionamiento.save()
                return redirect('InicioAdmin')
    return render(request, 'crearEstacionamiento.html',{'formEstacionamiento': EstacionamientoForm})
    

@login_required
def listarEstacionamientoDisponible(request):
    estacionamiento = Estacionamiento.objects.filter(estado = False)
    return render(request, 'listarEstacionamiento.html',{'estacionamientos':estacionamiento, 'title':'Estacionamientos disponibles'})

@login_required
def listarEstacionamientoNoDisponible(request):
    estacionamiento = Estacionamiento.objects.filter(estado = True)
    return render(request, 'listarEstacionamiento.html',{'estacionamientos':estacionamiento, 'title':'Estacionamientos No disponibles'})

@login_required
def generar_reporte_reservas(request):
    # Obtengo los datos de la base de datos
    reserva = Reserva.objects.all()
    data = {
        'count': reserva.count(),
        'reservas': reserva
    }
    return render_to_pdf('reportes.html', data) # Voy a buscar mi funcion desde el utils y le paso mi html y mis datos

@login_required
def selecionarReporte(request):
    busqueda = request.GET.get('desde')
    reservas = Reserva.objects.all()
    if busqueda:
        reservas = Reserva.objects.filter(fecha = busqueda) 

    return render(request, 'seleccionarReporte.html', {'reservas':reservas})

# @login_required
# def generarReserva(request):
# formReserva = ReservaForm()
#     return render(request, 'generarReserva.html',{'form': formReserva})

# @login_required
# def generarReserva(request):
#     estacionamiento = Estacionamiento.objects.filter(estado = False)
#     return render(request, 'generarReserva.html',{'estacionamientos':estacionamiento})

# def reservaUsuario(request, estacionamiento_id):
    
#     if request.method == 'POST':
#         formulario = EstacionamientosForm(request.POST)
#         if formulario.is_valid():
#             new_car = formulario.save(commit=False)
#             new_car.owner = request.user
#             new_car.numeroEstacionamiento = estacionamiento_id
#             new_car.save()
#             return redirect('generarReservaUsuario')
            
#     else:
#         return render(request, 'reservaUsuario.html', {'form':EstacionamientosForm})