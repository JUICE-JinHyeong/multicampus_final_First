from django.contrib import admin
from django.urls import path , include
from bbsApp import views

urlpatterns = [
    path("page/"    , views.page        , name = 'page') ,
    path("page/Minemine/"    , views.Minemine        , name = 'Minemine') ,
    path("page/Victoria/"    , views.Victoria        , name = 'Victoria') ,
    path("page/WelchsZ/"    , views.WelchsZ        , name = 'WelchsZ') ,
    path("page/ChilsungCiderZ/"    , views.ChilsungCiderZ        , name = 'ChilsungCiderZ') ,
    path("page/CocacolaZ/"    , views.CocacolaZ        , name = 'CocacolaZ') ,
    path("page/Trevi/"    , views.Trevi        , name = 'Trevi') ,
    path("page/NobrandSparkling/"    , views.NobrandSparkling        , name = 'NobrandSparkling') ,
    path("page/PepsiColaZ/"    , views.PepsiColaZ        , name = 'PepsiColaZ') ,
    path("page/BurrZcola/"    , views.BurrZcola        , name = 'BurrZcola') ,
    path("page/Reinwasser/"    , views.Reinwasser        , name = 'Reinwasser') ,
    path("page/Seagram/"    , views.Seagram        , name = 'Seagram') ,
    path("page/OneamSparkling/"    , views.OneamSparkling        , name = 'OneamSparkling') ,
    path("page/BurrZcider/"    , views.BurrZcider        , name = 'BurrZcider') ,
    path("page/NarangdCider/"    , views.NarangdCider        , name = 'NarangdCider') ,
    path("page/SpriteZ/"    , views.SpriteZ        , name = 'SpriteZ')

]

