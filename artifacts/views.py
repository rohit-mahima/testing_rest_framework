from rest_framework import viewsets
from .serializers import ArtifactSerializer
from .models import Artifiact

class ArtifactViewSet(viewsets.ModelViewSet):
    serializer_class=ArtifactSerializer

    def get_queryset(self):
        return Artifiact.objects.all()

    
    