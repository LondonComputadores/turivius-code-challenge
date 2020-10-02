"""
    This module sets up the model of this application.
    The Constant STATUS_CHOICE enables the field which has \
    the choices parameter set to create more than one option \
    from a drop dpwn menu on the GUI.
"""

from django.db import models

STATUS_CHOICES = [
    ('0', 'Loss'),
    ('1', 'Share'),
    ('2', 'Win'),
]

class Lawsuit(models.Model):
    """This sets up the fields of the database of the aplication"""
    n_processo = models.CharField(max_length=30, unique=True)
    id_cliente = models.IntegerField()    
    favor_contribuinte = models.CharField(max_length=1, choices=STATUS_CHOICES)
    ementa = models.TextField()

    def __str__(self):
        """Set the object that will be represented on searches"""
        #return self.n_processo  # uncomment this or may used as below:
        return '{}: - {}: - {}: - {}:'.format(self.n_processo, self.id_cliente,
                                            self.favor_contribuinte, self.ementa)