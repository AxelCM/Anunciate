#imports of django
from django.urls import path

#import from my apps
from anuncios.views import IndexView , CreateBulletin

urlpatterns = [
    path('' , IndexView.as_view() , name='index'),
    path('crear-anuncio' , CreateBulletin.as_view() , name='create_bulletin')
]
