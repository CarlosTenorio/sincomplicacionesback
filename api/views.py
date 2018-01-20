from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

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


class CountryViewSet(viewsets.ViewSet):
    """
    View to list all countries in the system.

    * Requires basic authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = (IsAdminUser,)

    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)

        return Response(serializer.data)

class CardViewSet(viewsets.ViewSet):
    """
    View to list all cards in the system and get the detail view.

    * Requires basic authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = (IsAdminUser,)

    def list(self, request):
        queryset = Card.objects.all()
        serializer = CardSerializer(queryset, many=True)

        return Response(serializer.data)

    def detail(self, request, card_id=None):
        queryset = Card.objects.all()
        card = get_object_or_404(queryset, pk=card_id)
        serializer = CardSerializer(card)

        return Response(serializer.data)


class ExpansionViewSet(viewsets.ViewSet):
    """
    View to list all expansions in the system.

    * Requires basic authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        queryset = Expansion.objects.all()
        serializer = ExpansionSerializer(queryset, many=True)

        return Response(serializer.data)


class ShippingViewSet(viewsets.ViewSet):
    """
    View to list all shippings in the system.

    * Requires basic authentication.
    * Only admin users are able to access this view.
    """
    permission_classes = (IsAdminUser,)

    def list(self, request):
        queryset = Shipping.objects.all()
        serializer = ShippingSerializer(queryset, many=True)

        return Response(serializer.data)
