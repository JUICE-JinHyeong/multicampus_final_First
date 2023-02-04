from django.contrib import admin
from django.urls import path, include
from zerosugarApp import views

urlpatterns = [
    path("",      views.index,        name="main") ,
    path("index/",      views.index,        name="main"),
    path("cocacola/",   views.cocacola,     name="product01"),
    path("pepsicola/",  views.pepsicola,    name="product02"),
    path("burrcola/",   views.burrcola,     name="product03"),
    path("sprite/",     views.sprite,       name="product04"),
    path("chilsung/",   views.chilsung,     name="product05"),
    path("burrcider/",  views.burrcider,    name="product06"),
    path("narangd/",    views.narangd,      name="product07"),
    path("nobrand/",    views.nobrand,      name="product08"),
    path("welchs/",     views.welchs,       name="product09"),
    path("oneam/",      views.oneam,        name="product10"),
    path("victoria/",   views.victoria,     name="product11"),
    path("minemine/",   views.minemine,     name="product12"),
    path("trevi/",      views.trevi,        name="product13"),
    path("reinwasser/", views.reinwasser,   name="product14"),
    path("seagram/",    views.seagram,      name="product15"),

    path("ajax/", views.Ajax, name="Ajax"),

    path("cocacola/grap", views.cocacola_subgrap, name="cocacola_subgrap"),
    path("pepsicola/grap", views.pepsicola_subgrap, name="pepsicola_subgrap"),
    path("burrcola/grap", views.burrcola_subgrap, name="burrcola_subgrap"),
    path("sprite/grap", views.sprite_subgrap, name="sprite_subgrap"),
    path("chilsung/grap", views.chilsung_subgrap, name="chilsung_subgrap"),
    path("burrcider/grap", views.burrcider_subgrap, name="burrcider_subgrap"),
    path("narangd/grap", views.narangd_subgrap, name="narangd_subgrap"),
    path("nobrand/grap", views.nobrand_subgrap, name="nobrand_subgrap"),
    path("welchs/grap", views.welchs_subgrap, name="welchs_subgrap"),
    path("oneam/grap", views.oneam_subgrap, name="oneam_subgrap"),
    path("victoria/grap", views.victoria_subgrap, name="victoria_subgrap"),
    path("minemine/grap", views.minemine_subgrap, name="minemine_subgrap"),
    path("trevi/grap", views.trevi_subgrap, name="trevi_subgrap"),
    path("reinwasser/grap", views.reinwasser_subgrap, name="reinwasser_subgrap"),
    path("seagram/grap", views.seagram_subgrap, name="seagram_subgrap")

]