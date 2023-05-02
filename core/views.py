from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    template_name = 'core/index.html'
    return render(request, template_name, data)