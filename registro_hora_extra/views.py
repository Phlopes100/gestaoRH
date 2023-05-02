from typing import Any, Dict
from .models import RegistroHoraExtra
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import HoraExtraForm
from django.urls import reverse_lazy

class HoraExtraList(ListView):
    template_name = 'registro_hora_extra/registro_hora_extra_list.html'
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
    
class HoraExtraCreate(CreateView):
    template_name = 'registro_hora_extra/registro_hora_extra_form.html'
    model = RegistroHoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEdit(UpdateView):
    template_name = 'registro_hora_extra/registro_hora_extra_form.html'
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraDelete(DeleteView):
    template_name = 'registro_hora_extra/registro_hora_extra_delete.html'
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')
    

