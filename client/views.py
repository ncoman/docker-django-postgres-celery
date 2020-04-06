from rest_framework import generics, permissions
from .models import Client
from .serializers import ClientSerializer


class ClientListView(generics.ListAPIView):
    """
    Retrieve List Objects
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

