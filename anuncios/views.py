#From django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView , CreateView
from django.contrib.auth import get_user_model , login , logout

User = get_user_model()

#import from my forms
from anuncios.forms import BulletinForm

#From MyModels
from anuncios.models import Bulletin
"""
Esta funcion nos va a desplegar nuestro nombre
de uuario dentro de un archivo HTML
"""

class IndexView(TemplateView):
    template_name = "anuncios/index.html"

    def get_context_data(self , *args , **kwargs):
        users = User.objects.all()
        bulletins = Bulletin.objects.all()
        return {'users': users , 'bulletins':bulletins}

class CreateBulletin(CreateView):
    template_name = "anuncios/forms/bulletin_form.html"
    form_class = BulletinForm
    success_url = reverse_lazy('index')

    def get_context_data(self, *args , **kwargs):
        """Agregar datos al contexto"""
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context
