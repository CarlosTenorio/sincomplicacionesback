from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from api.models import Country, Expansion, Card
from api.serializers import CountrySerializer, CardSerializer, ExpansionSerializer

#############################
# Default authentication #
# IsAuthenticatedOrReadOnly #
#############################

class CountryList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CardList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ExpansionList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer
