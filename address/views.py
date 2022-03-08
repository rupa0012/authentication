from rest_framework.viewsets import ModelViewSet
from .models import Address
from .serializer import AddressSeriazer

class AddressViewSet(ModelViewSet):
    serializer_class = AddressSeriazer
    queryset = Address.objects.all()


# Create your views here.
