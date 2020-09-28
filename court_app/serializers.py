from rest_framework import serializers
from court_app.models import Lawsuit

class LawsuitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lawsuit
        fields = ['pk', 'n_processo', 'id_cliente', 'favor_contribuinte', 'ementa']

    def natural_key(self):
        return (self.pk, self.n_processo, self.id_cliente, self.favor_contribuinte,
                                                               self.ementa)