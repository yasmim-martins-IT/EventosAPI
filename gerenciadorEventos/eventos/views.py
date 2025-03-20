from django.shortcuts import render
from .models import Eventos
from .serializers import EventosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils.timezone import now
import datetime 
from datetime import timedelta

@api_view(['GET'])
def listar_eventos(request):
  eventos = Eventos.objects.all()
  
  serializer = EventosSerializer(eventos, many = True)
  
  return Response(serializer.data)

@api_view(['GET'])
def listar_eventos_proximos(request):
   
  hoje = now().date() #pega a data de hoje

  limite = hoje + timedelta(days=7) #adiciona sete dias a data atual

  eventos = Eventos.objects.filter(data__range = [hoje , limite]) #filtra de hoje até sete dias
  serializer = EventosSerializer(eventos, many=True) #json dos eventos filtrados para daqui até sete dias
  
  return Response(serializer.data)

@api_view(['GET'])
def listar_evento(request,pk):
  evento = Eventos.objects.get(pk = pk)
  
  serializer = EventosSerializer(evento)

  return Response(serializer.data)

@api_view(['POST'])
def criar_eventos(request):
  if request.method == 'POST': 
    serializer = EventosSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED )
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def atualizar_eventos(request , pk):
  try :
    evento_atualizado = Eventos.objects.get(pk=pk)
  except Eventos.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  serializer = EventosSerializer(evento_atualizado,data = request.data , partial = True)
  
  if serializer.is_valid():
    serializer.save()
    
    return Response(serializer.data , status=status.HTTP_200_OK)
  return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_eventos(request, pk):
    try:
        evento_deletar = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    
    evento_deletar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

