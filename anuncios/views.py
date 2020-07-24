#From django
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model , login , logout

User = get_user_model()



#From MyModels

"""
Esta funcion nos va a desplegar nuestro nombre
de uuario dentro de un archivo HTML
"""

class PrimeraView(TemplateView):
    template_name = "anuncios/index.html"

    def get_context_data(self , *args , **kwargs):
        users = User.objects.all()
        return {'users': users}
