from rest_framework import viewsets

from api.models import UserExtended, Province, City
from api.serializers import UserSerializer, CitySerializer, ProvinceSerializer


class UserList(viewsets.ModelViewSet):
    queryset = UserExtended.objects.all()
    serializer_class = UserSerializer


class CityList(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    

class ProvinceList(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
