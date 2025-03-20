from django.urls import path
from . import views

urlpatterns =  [
  path('eventos/', views.listar_eventos),
  path('eventos/criar/', views.criar_eventos),
  path('eventos/atualizar/<int:pk>/',views.atualizar_eventos),
  path('eventos/deletar/<int:pk>/', views.deletar_eventos),
  path('eventos/proximos/', views.listar_eventos_proximos),
  path('eventos/<int:pk>/',views.listar_evento)
]