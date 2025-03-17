from django.shortcuts import render
from .models import Eventos
from .serializers import EventosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def listar_eventos(requst):
  eventos = Eventos.objects.all()
  
  serializer = EventosSerializer(eventos, many = True)
  
  return Response(serializer.data)

@api_view(['POST'])
def criar_eventos(request):
  if request.method == 'post': 
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
def deletar_eventos (request, pk):
  try :
    evento_deletar = Eventos.objects.get(pk=pk)
  except Eventos.DoesNotExist:
    return Response(status=status.HTTP_403_FORBIDDEN)
  
  evento_deletar.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)