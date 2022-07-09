from rest_framework.decorators import api_view
from rest_framework.response import Response
from vehicles.models import Tool
from vehicles.serializers.tools import TooSerializer

@api_view(["GET"])
def list_tools(request):
    tools=[
        Tool("hammer", "mastercraft"),
        Tool("wrench","husky"),
    ]

    serializer= TooSerializer(tools, many=True)

    content ={
        "tools": serializer.data
    }

    return Response(content)