from django.conf.urls import url
from rest_framework.authtoken import views
from api import views as api_views

card_list = api_views.CardList.as_view({
    'get': 'list',
    'post': 'create'
})

country_list = api_views.CountryList.as_view({
    'get': 'list',
    'post': 'create'
})

expansion_list = api_views.ExpansionList.as_view({
    'get': 'list',
    'post': 'create'
})

shipping_list = api_views.ShippingList.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'^cards/$', card_list, name='card-list'),
    url(r'^countries/$', country_list, name='country-list'),
    url(r'^expansions/$', expansion_list, name='expansion-list'),
    url(r'^shippings/$', shipping_list, name='shipping-list'),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
