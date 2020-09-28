from django.db import models

STATUS_CHOICES = [
    ('0', 'Loss'),
    ('1', 'Share'),
    ('2', 'Win'),
]

class Lawsuit(models.Model):
    n_processo = models.CharField(max_length=30, unique=True)
    id_cliente = models.IntegerField()    
    favor_contribuinte = models.CharField(max_length=1, choices=STATUS_CHOICES)
    ementa = models.TextField()

    def __str__(self):
        return self.n_processo