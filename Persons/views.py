from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import People

@api_view(["GET"])
def list_people(request):
    people=People.objects.all()
    serializer=PersonSerializer(people, many=True)
    content={
        "people":serializer.data,
    }

    return Response(content)
