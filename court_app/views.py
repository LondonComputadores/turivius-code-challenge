from rest_framework import viewsets
from court_app.models import Lawsuit
from court_app.serializers import LawsuitSerializer

class LawsuitViewSet(viewsets.ModelViewSet):
    """Set the view of the application with its objects serialized"""
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitSerializer
