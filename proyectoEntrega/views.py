from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from flia.models import Familia






def crear_persona(request):
    
    persona1 = Familia(nombre='Ricardo' , apellido='Darin' , edad=random.randrange(1, 99) , fecha_nacimiento=datetime.now())
    persona2 = Familia(nombre='Patricio' , apellido='Darin' , edad=random.randrange(1, 99) , fecha_nacimiento=datetime.now())                  
    persona3 = Familia(nombre='Josefina' , apellido='Darin' , edad=random.randrange(1, 99) , fecha_nacimiento=datetime.now())
                       
    persona1.save()
    persona2.save()
    persona3.save()  
    
    
    template = loader.get_template('crear_personas.html')
    template_renderizado = template.render({})                      
    
    
    return HttpResponse(template_renderizado)




def ver_personas(request):
    
    personas = Familia.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)

