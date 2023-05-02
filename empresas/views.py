from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa
# Create your views here.

class EmpresaCreate(CreateView):
    template_name = 'empresas/empresa_form.html'
    model = Empresa
    fields = ['nome']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        
    

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
    success_url = reverse_lazy('home')
