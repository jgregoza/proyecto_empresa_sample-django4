from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento
from .forms import NewDepartmentForm

# Create your views here.


class DepartamentoListView(ListView):
    template_name = "departamento/lista_departamento.html"
    model = Departamento
    context_object_name = 'departamentos'

    
class NewDepartmentoView(FormView):
    template_name = 'departamento/nuevo_departamento.html'
    form_class = NewDepartmentForm
    success_url = reverse_lazy("departamento_app:lista_departamento")

    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']    #recuperando los datos desde el form
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job='1',
            departamento=depa,
        )
        return super(NewDepartmentoView, self).form_valid(form)