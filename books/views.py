from rest_framework import viewsets
from .serializers import BookSerializers
from rest_framework import permissions
from .models import Book
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializers
    permission_classes=[permissions.IsAuthenticated, permissions.IsAdminUser]
    queryset=Book.objects.all()

@login_required
def library(request):
    output=f"""
    <html>
    <body>
    <h2> Library </h2>
    <p> { request.user.username } </p>
    <a href = "/books/"> Book API </a>
    </body>
    </html>
    
    """

    return HttpResponse(output)

