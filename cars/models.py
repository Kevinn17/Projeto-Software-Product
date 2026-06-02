from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='car_marca')
    fabricado_em = models.IntegerField(blank=True, null=True)
    ano_modelo = models.IntegerField(blank=True, null=True)
    placa = models.CharField(max_length=10, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)
    foto = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.modelo
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_valor= models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.created_at} - {self.cars_count} carros'

class Agendamento(models.Model):
    TIPOS = [
        ('visita', 'Visita'),
        ('test_drive', 'Test Drive'),
    ]

    STATUS = [
        ("pendente","Pendente"),
        ("confirmado","Confirmado"),
        ("cancelado","Cancelado"),
        ("expirado","Expirado"),
    ]

    carro = models.ForeignKey("Car", on_delete=models.CASCADE)
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=20)
    data_hora = models.DateTimeField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    status = models.CharField(max_length=20, choices=STATUS, default="pendente")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_cliente} - {self.carro} - {self.data_hora}"

