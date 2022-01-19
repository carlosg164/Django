from datetime import date, datetime
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
import datetime


def index(request):

    miki="miki"
    #documento = open("/home/devipott/Documentos/Django/organizador/organizador/plantillas/index.html")
    #plantilla = Template(documento.read())
    fecha=datetime.datetime.now()
    #documento.close()
    #documento = loader.get_template("index.html")
    #contexto = Context({"nombre":miki, "fecha":fecha})
    #doc=documento.render({"nombre":miki, "fecha":fecha})
    #Modificar archivo settings en un proyecto nuevo
    return render(request,"index.html", {"nombre":miki, "fecha":fecha})