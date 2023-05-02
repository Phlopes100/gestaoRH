from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionariosList(ListView):
    template_name = 'funcionarios/funcionarios_list.html'
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionarioNovo(CreateView):
    template_name = 'funcionarios/funcionarios_novo.html'
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('list_funcionarios')
    
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


class FuncionarioEdit(UpdateView):
    template_name = 'funcionarios/funcionarios_form.html'
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    template_name = 'funcionarios/funcionarios_delete.html'
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
