from django.shortcuts import render,redirect
from .models import *

def Minemine(request) :
    print('debug >>>>>> method GET path : show/ , render : bbs/Minemine.html')
    return render(request , 'bbs/page/Minemine.html')

def Victoria(request) :
    print('debug >>>>>> method GET path : show/ , render : bbs/Victoria.html')
    return render(request , 'bbs/page/Victoria.html')

def WelchsZ(request) :
    print('debug >>>>>> method GET path : show/ , render : bbs/WelchsZ.html')
    return render(request , 'bbs/page/WelchsZ.html')

def ChilsungCiderZ(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/ChilsungCiderZ.html')
    return render(request, 'bbs/page/ChilsungCiderZ.html')

def CocacolaZ(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/CocacolaZ.html')
    return render(request, 'bbs/page/CocacolaZ.html')

def Trevi(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/Trevi.html')
    return render(request, 'bbs/page/Trevi.html')

def NobrandSparkling(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/NobrandSparkling.html')
    return render(request, 'bbs/page/NobrandSparkling.html')

def PepsiColaZ(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/PepsiColaZ.html')
    return render(request, 'bbs/page/PepsiColaZ.html')

def BurrZcola(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/BurrZcola.html')
    return render(request, 'bbs/page/BurrZcola.html')

def Reinwasser(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/Reinwasser.html')
    return render(request, 'bbs/page/Reinwasser.html')

def Seagram(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/Seagram.html')
    return render(request, 'bbs/page/Seagram.html')

def OneamSparkling(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/OneamSparkling.html')
    return render(request, 'bbs/page/OneamSparkling.html')

def BurrZcider(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/BurrZcider.html')
    return render(request, 'bbs/page/BurrZcider.html')

def NarangdCider(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/NarangdCider.html')
    return render(request, 'bbs/page/NarangdCider.html')

def SpriteZ(request):
    print('debug >>>>>> method GET path : show/ , render : bbs/SpriteZ.html')
    return render(request, 'bbs/page/SpriteZ.html')
