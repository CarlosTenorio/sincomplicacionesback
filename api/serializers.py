from rest_framework import serializers
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
        fields = ('date', 'shipping_type', 'shipping_costs', 'shipping_card')

    def create(self, validated_data):
        cards_data = validated_data.pop('shipping_card')
        print(validated_data)
        shipping = Shipping.objects.create(**validated_data)
        for card_data in cards_data:
            country = card_data.get('country', card_data['country'].id)
            expansion = card_data.get('expansion', card_data['expansion'].id)
            Card.objects.create(
                shipping=shipping,
                country=country,
                title=card_data['title'],
                description=card_data['description']
            )
        return shipping
