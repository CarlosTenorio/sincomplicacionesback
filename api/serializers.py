from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from api.models import Country, Card, Expansion, Shipping

from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class ExpansionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expansion
        fields = '__all__'


class ShippingSerializer(serializers.ModelSerializer):
    shipping_card = CardSerializer(many=True)

    class Meta:
        model = Shipping
        fields = ('id', 'date', 'type', 'costs',
            'shipping_card', 'user')

    def create(self, validated_data):
        user = self.context['request'].user
        cards_data = validated_data.pop('shipping_card')
        shipping = Shipping.objects.create(
            date = validated_data['date'],
            type = validated_data['type'],
            costs = validated_data['costs'],
            user = user
        )
        for card_data in cards_data:
            country = card_data.get('country', card_data['country'].id)
            expansion = card_data.get('expansion', card_data['expansion'].id)
            Card.objects.create(
                shipping = shipping,
                country = country,
                expansion = expansion,
                title = card_data['title'],
                description = card_data['description'],
                price = card_data['price']
            )
        return shipping
