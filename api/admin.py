from django.contrib import admin

from api.models import Category, City, Country, Province, PostalCode, UserExtended

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(PostalCode)
admin.site.register(Province)
admin.site.register(UserExtended)
