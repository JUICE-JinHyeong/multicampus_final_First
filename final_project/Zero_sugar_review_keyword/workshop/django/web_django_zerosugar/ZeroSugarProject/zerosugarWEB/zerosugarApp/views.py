from django.shortcuts import render

# Create your views here.


import pandas as pd

from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def index(request) :
    return render(request, 'zerosugar/index.html')

def cocacola(request) :
    return render(request, 'zerosugar/product01.html')

def pepsicola(request) :
    return render(request, 'zerosugar/product02.html')

def burrcola(request) :
    return render(request, 'zerosugar/product03.html')

def sprite(request) :
    return render(request, 'zerosugar/product04.html')

def chilsung(request) :
    return render(request, 'zerosugar/product05.html')

def burrcider(request) :
    return render(request, 'zerosugar/product06.html')

def narangd(request) :
    return render(request, 'zerosugar/product07.html')

def nobrand(request) :
    return render(request, 'zerosugar/product08.html')

def welchs(request) :
    return render(request, 'zerosugar/product09.html')

def oneam(request) :
    return render(request, 'zerosugar/product10.html')

def victoria(request) :
    return render(request, 'zerosugar/product11.html')

def minemine(request) :
    return render(request, 'zerosugar/product12.html')

def trevi(request) :
    return render(request, 'zerosugar/product13.html')

def reinwasser(request) :
    return render(request, 'zerosugar/product14.html')

def seagram(request) :
    return render(request, 'zerosugar/product15.html')


def Ajax (request) :
    return render(request, 'ajax_file/Ajax.json')


def cocacola_subgrap(request):
    return render(request , 'subgrap/product01_subgrap.html')
def pepsicola_subgrap(request):
    return render(request , 'subgrap/product02_subgrap.html')
def burrcola_subgrap(request):
    return render(request , 'subgrap/product03_subgrap.html')
def sprite_subgrap(request):
    return render(request , 'subgrap/product04_subgrap.html')
def chilsung_subgrap(request):
    return render(request , 'subgrap/product05_subgrap.html')
def burrcider_subgrap(request):
    return render(request , 'subgrap/product06_subgrap.html')
def narangd_subgrap(request):
    return render(request , 'subgrap/product07_subgrap.html')
def nobrand_subgrap(request):
    return render(request , 'subgrap/product08_subgrap.html')
def welchs_subgrap(request):
    return render(request , 'subgrap/product09_subgrap.html')
def oneam_subgrap(request):
    return render(request , 'subgrap/product10_subgrap.html')
def victoria_subgrap(request):
    return render(request , 'subgrap/product11_subgrap.html')
def minemine_subgrap(request):
    return render(request , 'subgrap/product12_subgrap.html')
def trevi_subgrap(request):
    return render(request , 'subgrap/product13_subgrap.html')
def reinwasser_subgrap(request):
    return render(request , 'subgrap/product14_subgrap.html')
def seagram_subgrap(request):
    return render(request , 'subgrap/product15_subgrap.html')






