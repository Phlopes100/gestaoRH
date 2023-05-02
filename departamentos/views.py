from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento

class DepartamentoList(ListView):
    template_name = 'departamentos/departamento_list.html'
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    template_name = 'departamentos/departamento_form.html'
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)
    
class DepartamentoUpdate(UpdateView):
    template_name = 'departamentos/departamento_form.html'
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')


class DepartamentoDelete(DeleteView):
    template_name = 'departamentos/departamento_delete.html'
    model = Departamento
    success_url = reverse_lazy('list_departamentos')