from rest_framework import serializers
from court_app.models import Lawsuit

class LawsuitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lawsuit
        fields = ['url', 'n_processo', 'id_cliente', 'favor_contribuinte', 'ementa']