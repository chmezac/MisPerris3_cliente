from django.db import models

# Create your models here.

class Perris( models.Model ):

    DISPONIBLE = 'Disponible'
    ADOPTADO = 'Adoptado'
    RESCATADO = 'Rescatado'
    
    STATE_CHOICES = (
        (DISPONIBLE, 'Disponible'),
        (ADOPTADO, 'Adoptado'),
        (RESCATADO, 'Rescatado'),
    )

    id = models.AutoField( primary_key = True )
    nombre = models.CharField( max_length = 50, default = '' )
    raza = models.CharField( max_length = 30, default = '' )
    descripcion = models.TextField( default= '' )
    state = models.CharField( max_length=10, choices=STATE_CHOICES, default=RESCATADO)
    imageUrl = models.CharField( max_length = 255, default = '' )

    def __str__( self ):
        return self.nombre




    