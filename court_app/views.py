from rest_framework import viewsets
from court_app.models import Lawsuit
from court_app.serializers import LawsuitSerializer

class LawsuitViewSet(viewsets.ModelViewSet):
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitSerializer
