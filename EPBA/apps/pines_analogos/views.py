from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class pines_analogos(TemplateView):
    template_name = "teoria/pines_analogos/pines_analogos.html"

class ejemplo1(TemplateView):
    template_name = "teoria/pines_analogos/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/pines_analogos/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/pines_analogos/ejemplos/ejemplo3.html"

class ejemplo4(TemplateView):
    template_name = "teoria/pines_analogos/ejemplos/ejemplo4.html"

class ejemplo5(TemplateView):
    template_name = "teoria/pines_analogos/ejemplos/ejemplo5.html"

class ejemplo6(TemplateView):
    template_name = "teoria/pines_analogos/ejemplos/ejemplo6.html"