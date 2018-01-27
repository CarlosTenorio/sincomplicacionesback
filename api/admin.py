from django.contrib import admin
from api.models import Country, Card, Expansion, Shipping

admin.site.register(Expansion)
admin.site.register(Card)
admin.site.register(Country)
admin.site.register(Shipping)
