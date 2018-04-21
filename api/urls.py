from django.conf.urls import url
from rest_framework.authtoken import views
from api import views as api_views

card_list = api_views.CardViewSet.as_view({'get': 'list'})
card_detail = api_views.CardViewSet.as_view({'get': 'detail'})

country_list = api_views.CountryViewSet.as_view({'get': 'list'})

expansion_list = api_views.ExpansionViewSet.as_view({'get': 'list'})

shipping_list = api_views.ShippingViewSet.as_view({'get': 'list', 'post': 'create'})
shipping_detail = api_views.ShippingViewSet.as_view({'get': 'detail'})

urlpatterns = [
    url(r'^cards/$', card_list, name='card-list'),
    url(r'^card/(?P<card_id>[0-9]+)/$', card_detail, name='card-detail'),
    url(r'^countries/$', country_list, name='country-list'),
    url(r'^expansions/$', expansion_list, name='expansion-list'),
    url(r'^shippings/$', shipping_list, name='shipping-list'),
    url(r'^shippings/(?P<shipping_id>[0-9]+)/$', shipping_detail, name='shipping-detail'),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
