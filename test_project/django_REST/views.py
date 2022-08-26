# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import AccountSerializer
from .models import AccountModel


# create a viewset
class AccountViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = AccountModel.objects.all()

    # specify serializer to be used
    serializer_class = AccountSerializer
