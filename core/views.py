from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    context= {
        "courses" : Course.objects.all()
    }
    return render(request, "core/index.html", context)

def create_course(request):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        # pasar los datos al método que escribimos y guardar la respuesta en una variable llamada errores
        errors = Course.objects.basic_validator(request.POST)
        # compruebe si el diccionario de errores tiene algo en él
        if len(errors) > 0:
            # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
            # redirigir al usuario al formulario para corregir los errores
            return redirect("/")
        else:
            name = request.POST["name"]
            desc = request.POST["desc"]
            obj = Course.objects.create(name=name, desc=desc)
            obj.save()
            messages.success(request, "Course created successfully!!!")
            return redirect("/")

def destroy_course(request, course_id):
    context = {
        "id" : Course.objects.get(id=course_id).id,
        "name" : Course.objects.get(id=course_id).name,
        "desc" : Course.objects.get(id=course_id).desc
    }
    return render(request, "core/destroy.html", context)

def delete_course(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect("/")