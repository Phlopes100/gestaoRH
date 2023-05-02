from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView
from .models import Documento

class DocumentoCreate(CreateView):
    template_name = 'documentos/documento_form.html'
    model = Documento
    fields = ['descricao', 'arquivo']
    success_url = 'update_funcionario'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)