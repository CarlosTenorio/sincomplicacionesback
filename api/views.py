from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny,
    IsAuthenticatedOrReadOnly

from api.models import UserExtended, Province, City
from api.serializers import UserSerializer, CitySerializer, ProvinceSerializer

#############################
# Default authentication #
# IsAuthenticatedOrReadOnly #
#############################

class UserList(viewsets.ModelViewSet):
    queryset = UserExtended.objects.all()
    serializer_class = UserSerializer


class CityList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = City.objects.all()
    serializer_class = CitySerializer


class ProvinceList(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
