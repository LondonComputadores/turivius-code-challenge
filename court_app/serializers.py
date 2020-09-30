from rest_framework import serializers
from court_app.models import Lawsuit

class LawsuitSerializer(serializers.HyperlinkedModelSerializer):
    """Allow to choose only the fields that will be visible on API"""
    class Meta:
        model = Lawsuit
        fields = ['n_processo', 'id_cliente', 'favor_contribuinte', 'ementa']

    def natural_key(self):
        return (self.pk, self.n_processo, self.id_cliente, self.favor_contribuinte,
                                                               self.ementa)