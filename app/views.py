from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Welcome")

def suma(request,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = 'La suma de %i + %i = %i' % (num1,num2, num1+num2)
    return HttpResponse(result)

def resta(request,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = 'La resta de %i - %i = %i' % (num1,num2, num1-num2)
    return HttpResponse(result)

def multiplicacion(request,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = 'La multiplicacion de %i * %i = %i' % (num1,num2, num1*num2)
    return HttpResponse(result)