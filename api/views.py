from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token

from api.models import Country, Expansion, Card, Shipping
from api.serializers import CountrySerializer, CardSerializer, ExpansionSerializer, ShippingSerializer
from rest_framework.pagination import PageNumberPagination

#############################
# Default authentication #
# IsAuthenticatedOrReadOnly #
#############################
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class CountryList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CardList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ExpansionList(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = LargeResultsSetPagination

    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer


class ShippingList(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)

    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
