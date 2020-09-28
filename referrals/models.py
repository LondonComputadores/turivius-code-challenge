from django.db import models
from court_app.models import Lawsuit

class Referral(models.Model):
    numero = models.ForeignKey(Lawsuit, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero