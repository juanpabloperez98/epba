from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class pwm(TemplateView):
    template_name = "teoria/pwm/pwm.html"

class ejemplo1(TemplateView):
    template_name = "teoria/pwm/ejemplos/ejemplo1.html"

class ejemplo2(TemplateView):
    template_name = "teoria/pwm/ejemplos/ejemplo2.html"

class ejemplo3(TemplateView):
    template_name = "teoria/pwm/ejemplos/ejemplo3.html"

class ejemplo4(TemplateView):
    template_name = "teoria/pwm/ejemplos/ejemplo4.html"

class ejemplo5(TemplateView):
    template_name = "teoria/pwm/ejemplos/ejemplo5.html"

class ejemplo6(TemplateView):
    template_name = "teoria/pwm/ejemplos/ejemplo6.html"