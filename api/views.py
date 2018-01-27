from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from api.models import Country, Expansion, Card, Shipping
from api.serializers import CountrySerializer, CardSerializer, ExpansionSerializer, ShippingSerializer


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

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    def list(self, request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)

        return Response(serializer.data)


class CardViewSet(viewsets.ViewSet):
    """
    View to list all cards in the system and get the detail view.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
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

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        queryset = Expansion.objects.all()
        serializer = ExpansionSerializer(queryset, many=True)

        return Response(serializer.data)


class ShippingViewSet(viewsets.ViewSet):
    """
    View to list all shippings in the system.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """
    def list(self, request):
        queryset = Shipping.objects.filter(user=request.user)
        serializer = ShippingSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = ShippingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
