from django.db import models
import datetime

class Eventos (models.Model):
  nome = models.CharField(max_length=200)
  descricao = models.TextField()
  data = models.DateField()
  local = models.TimeField(null = True, blank= True )
  categoria = models.TextField(null = True , blank= True)
  
  
  def __str__(self):
    return self.nome
  
  # Create your models here.
