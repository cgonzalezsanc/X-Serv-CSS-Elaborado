from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def handler(request, recurso):
    fila = Pages.objects.filter(name=recurso)
    if request.method == "GET":
        if not fila:
            return HttpResponseNotFound("Pagina no encontrada")
        else:
            return HttpResponse(fila[0].page)
    elif request.method == "PUT":
        if not fila:
            page = "<html>\n\t<head>\n\t\t<link rel='stylesheet'"
            page += "media='screen' href='/css/main.css'>\n\t</head>\n\n\t"
            page += "<body>\n\t\t" + request.body + "\n\t</body>\n</html>"
            fila = Pages(name=recurso, page=page)
            fila.save()
            return HttpResponse(fila.page)
        else:
            return HttpResponse("Esta pagina ya esta almacenada")
    else:
        return HttpResponseNotFound("Metodo erroneo")

@csrf_exempt      
def css_handler(request, recurso):
    fila = Pages.objects.filter(name=recurso)
    if request.method == "GET":
        if not fila:
            return HttpResponseNotFound("Pagina no encontrada")
        else:
            return HttpResponse(fila[0].page, content_type="text/css")
    elif request.method == "PUT":
        if not fila:
            fila = Pages(name=recurso, page=request.body)
            fila.save()
            return HttpResponse(fila.page)
        else:
            return HttpResponse("Esta pagina ya esta almacenada")
    else:
        return HttpResponseNotFound("Metodo erroneo")
