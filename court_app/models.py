from django.db import models

class Lawsuits(models.Model):
    lawsuit_number = models.CharField(max_length=30, unique=True)
    summarization = models.TextField()
    # verdict_probability = models.CharField({
    #     'julgado': '0',
    #     'parcialmente favorável': '1',
    #     'favorável': '2'
    # })

    def __str__(self):
        return self.lawsuit_number