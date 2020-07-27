from django import forms

from anuncios.models import Bulletin

class BulletinForm(forms.ModelForm):

    class Meta:
        model = Bulletin
        fields = ['title' , 'price' , 'description']
        
