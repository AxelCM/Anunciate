from django.db import models

# Create your models here.
class Bulletin(models.Model):
    title = models.CharField('Titulo' , max_length=50)
    price = models.IntegerField('Precio')
    description = models.TextField('Descripcion')

    def __str__(self):
        return "{} Q.{}".format(self.title , self.price)
