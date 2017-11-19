from rest_framework import serializers
from api.models import UserExtended, City, Province


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExtended
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
