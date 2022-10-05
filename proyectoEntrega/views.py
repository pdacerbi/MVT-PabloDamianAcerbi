from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from flia.models import Familia






def crear_persona(request):
    
    persona1 = Familia(nombre='Ricardo' , apellido='Darin' , edad = 60 , fecha_nacimiento=datetime(1962, 5, 3))
    persona2 = Familia(nombre='Patricio' , apellido='Darin' , edad = 45, fecha_nacimiento=datetime(1977, 8, 1))      
    persona3 = Familia(nombre='Josefina' , apellido='Darin' , edad = 8, fecha_nacimiento=datetime(2014, 9, 21))
                       
    persona1.save()
    persona2.save()
    persona3.save()  
    
    
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'personas' : persona1 })     
    template_renderizado = template.render({'personas' : persona2 })  
    template_renderizado = template.render({'personas' : persona3 })                   
    
    
    return HttpResponse(template_renderizado)




def ver_personas(request):
    
    personas = Familia.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)

